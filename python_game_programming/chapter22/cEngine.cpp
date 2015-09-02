#include "Python.h"
#include "engine.h"


GraphicsEngine *gEngine = NULL;


/* 
**  structure definition for GraphicsObject wrapper
*/
typedef struct {
  PyObject_HEAD
  GraphicsObject *m_gObject;
} py_GraphicsObject;

/*
**   Deallocation function for GraphicsObject
*/
static void py_GraphicsObject_dealloc(PyObject* self)
{
  py_GraphicsObject *gobj = (py_GraphicsObject*)self;
  if (gobj->m_gObject)
  {
    delete gobj->m_gObject;
    gobj->m_gObject = NULL;
  }
  PyObject_Del(self);
}

/*
** GraphicsObject getSimData method
*/
PyObject *py_getSimData( PyObject *self, PyObject *args)
{
  return PyInt_FromLong(1);
}

/*
** GraphicsObject setState method
*/
PyObject *py_setState( PyObject *self, PyObject *args)
{
  return PyInt_FromLong(1);
}

/*
** GraphicsObject setFrame method
*/
PyObject *py_setFrame( PyObject *self, PyObject *args)
{
  return PyInt_FromLong(1);
}

/*
** GraphicsObject nextFrame method
*/
PyObject *py_nextFrame( PyObject *self, PyObject *args)
{
  return PyInt_FromLong(1);
}

/*
** GraphicsObject destroy method
*/
PyObject *py_destroy( PyObject *self, PyObject *args)
{
  return PyInt_FromLong(1);
}

/*
** GraphicsObject Method Table
*/
PyMethodDef py_GraphicsObject_methods[] = {
  {"getSimData",   py_getSimData, METH_VARARGS},
  {"setState",     py_setState,   METH_VARARGS},
  {"setFrame",     py_setFrame,   METH_VARARGS},
  {"nextFrame",    py_nextFrame,  METH_VARARGS},
  {"destroy",      py_destroy,    METH_VARARGS},
  {NULL,           NULL,             NULL},
};

/*
**  GraphicsObject getattr function
**
*/
PyObject *py_getattr(PyObject *self, char *attrname)
{ 
  py_GraphicsObject *obj = (py_GraphicsObject*)self;
  PyObject *result = Py_FindMethod(py_GraphicsObject_methods, self, attrname);
  return result;
}

/*
**  GraphicsObject type object
**
*/
static PyTypeObject py_GraphicsObject_Type = {
    PyObject_HEAD_INIT(NULL)
    0,                          /* number of items */
    "GraphicsObject",           /* type name */
    sizeof(py_GraphicsObject),  /* basic size of instances */
    0,                          /* item size */
    py_GraphicsObject_dealloc,  /* deallocation function_dealloc*/
    0,                          /* print function - tp_print*/
    py_getattr,                 /* getattr function - tp_getattr*/
    0,                          /* setattr function - tp_setattr */
    0,                          /* comparison function - tp_compare*/
    0,                          /* repr function - tp_repr*/
    0,                          /* tp_as_number*/
    0,                          /* tp_as_sequence*/
    0,                          /* tp_as_mapping*/
    0,                          /* tp_hash */
};


/*
**  GraphicsObject Creation Function
**
*/
PyObject *py_new_GraphicsObject( PyObject *, PyObject *args)
{
  char *source;
  bool mobile;
  char *image = NULL;
  
  if (!PyArg_ParseTuple(args, "si|s:GraphicsObject", &source, &mobile, &image) )
  {
    return NULL;
  }
  
  // Create the Python wrapper object
  py_GraphicsObject *gObj = PyObject_New(py_GraphicsObject,&py_GraphicsObject_Type);

  // Create the actual graphics object
  gObj->m_gObject = new GraphicsObject(source, mobile, image);

  return (PyObject*)gObj;
}


/*
** py_initialize()
**
** Params:   width and height
** Returns:  1
*/
PyObject *py_initialize( PyObject *, PyObject *args )
{
  int width, height;
  
  if( !PyArg_ParseTuple(args, "ii:py_initialize", &width, &height) )
  {
    return NULL;
  }

  if (gEngine)
  {
    PyErr_SetString(PyExc_AttributeError, "Engine already initialized");
    return NULL;
  }
  
  gEngine = new GraphicsEngine(width, height);
  return PyInt_FromLong(1);
}

/*
** py_shutdown()
**
** Params:   
** Returns:  0 or 1
*/
PyObject *py_shutdown( PyObject *, PyObject *args )
{
  if (gEngine)
  {
    delete gEngine;
    gEngine = NULL;
    return PyInt_FromLong(1);
  }
  else
  { 
    PyErr_SetString(PyExc_AssertionError, "Engine not initialized");
    return NULL;
 }
}


/*
** py_addObject()
**
** Param:   object - the graphics object
** Param:   x      - the X position of the object
** Param:   y      - the Y position of the object
** Param:   facing - the object's facing direction
** Returns:  0 or 1
*/
PyObject *py_addObject( PyObject *, PyObject *args )
{
  
  PyObject *obj;
  float x, y, facing;

  if (!gEngine)
  {
    PyErr_SetString(PyExc_AssertionError, "Engine not initialized");
    return NULL;
  }

  if( !PyArg_ParseTuple(args, "Offf:py_addObject", &obj, &x, &y, &facing) )
  {
    return NULL;
  }

  if (!PyObject_TypeCheck(obj, &py_GraphicsObject_Type)  )
  {
    PyErr_SetString(PyExc_AssertionError, "object must be a graphics object");
    return NULL;
  }
  
  py_GraphicsObject *gObject = (py_GraphicsObject*)obj;
  gEngine->addObject(gObject->m_gObject, x, y, facing);
  
  return PyInt_FromLong(1);  
}



/*
** py_removeObject()
**
** Param:   object - the graphics object
** Returns:  0 or 1
*/
PyObject *py_removeObject( PyObject *, PyObject *args )
{
  PyObject *obj;

  if (!gEngine)
  {
    PyErr_SetString(PyExc_AssertionError, "Engine not initialized");
    return NULL;
  }

  if( !PyArg_ParseTuple(args, "O:removeObject", &obj) )
  {
    return NULL;
  }

  if (!PyObject_TypeCheck(obj, &py_GraphicsObject_Type)  )
  {
    PyErr_SetString(PyExc_AssertionError, "object must be a graphics object");
    return NULL;
  }
  
  py_GraphicsObject *gObject = (py_GraphicsObject*)obj;
  gEngine->removeObject(gObject->m_gObject);

  return PyInt_FromLong(1);  
}


/*
** py_render()
**
** Params:   
** Returns: nothing
*/
PyObject *py_render( PyObject *, PyObject *args )
{
  if (!gEngine)
  { 
    PyErr_SetString(PyExc_AssertionError, "Engine not initialized");
    return NULL;
 }

  gEngine->render();
  return PyInt_FromLong(1);  
}


/*
** py_setView()
**
** Param:   x - view X position
** Param:   y - view Y position
** Returns: 1
*/
PyObject *py_setView( PyObject *, PyObject *args )
{
  int posX, posY;

  if (!gEngine)
  { 
    PyErr_SetString(PyExc_AssertionError, "Engine not initialized");
    return NULL;
  }

  if( !PyArg_ParseTuple(args, "ii:py_setView", &posX, &posY) )
  {
    return NULL;
  }

  gEngine->setView(posX, posY);
  return PyInt_FromLong(1);  
}


/*
** py_getWidth()
**
** Param:   none
** Returns: engine width
*/
PyObject *py_getWidth( PyObject *, PyObject *args )
{
  if (!gEngine)
  { 
    PyErr_SetString(PyExc_AssertionError, "Engine not initialized");
    return NULL;
  }

  int width = gEngine->getWidth();
  return PyInt_FromLong(width);  
}

/*
** py_getHeight()
**
** Param:   none
** Returns: engine height
*/
PyObject *py_getHeight( PyObject *, PyObject *args )
{
  if (!gEngine)
  { 
    PyErr_SetString(PyExc_AssertionError, "Engine not initialized");
    return NULL;
  }

  int height = gEngine->getHeight();
  return PyInt_FromLong(height);  
}

/*
** py_worldToScreen()
**
** Param:   world X 
** Param:   world Y
** Returns: (screenX, screenY)
*/
PyObject *py_worldToScreen( PyObject *, PyObject *args )
{
  float worldX, worldY;
  float screenX, screenY;

  if (!gEngine)
  { 
    PyErr_SetString(PyExc_AssertionError, "Engine not initialized");
    return NULL;
  }

  if( !PyArg_ParseTuple(args, "ff:py_worldToScreen", &worldX, &worldY) )
  {
    return NULL;
  }
  
  gEngine->worldToScreen(worldX, worldY, screenX, screenY);

  return Py_BuildValue("ii", screenX, screenY);
}

/*
** py_screenToWorld()
**
** Param:   screen X 
** Param:   screen Y
** Returns: (worldX, worldY)
*/
PyObject *py_screenToWorld( PyObject *, PyObject *args )
{
  float worldX, worldY;
  float screenX, screenY;

  if (!gEngine)
  { 
    PyErr_SetString(PyExc_AssertionError, "Engine not initialized");
    return NULL;
  }

  if( !PyArg_ParseTuple(args, "ff:py_screenToWorld", &screenX, &screenY) )
  {
    return NULL;
  }
  
  gEngine->screenToWorld(screenX, screenY, worldX, worldY);

  return Py_BuildValue("ii", worldX, worldY);
}


/*
** py_getSources()
**
** Params:   
** Returns: nothing
*/
PyObject *py_getSources( PyObject *, PyObject *args )
{
  if (!gEngine)
  { 
    PyErr_SetString(PyExc_AssertionError, "Engine not initialized");
    return NULL;
 }

  PyErr_SetString(PyExc_NotImplementedError, "getSources not available");
  return NULL;
}


/*
** py_getTextures()
**
** Params:   
** Returns: nothing
*/
PyObject *py_getTextures( PyObject *, PyObject *args )
{
  if (!gEngine)
  { 
    PyErr_SetString(PyExc_AssertionError, "Engine not initialized");
    return NULL;
  }

  PyErr_SetString(PyExc_NotImplementedError, "getTextures not available");
  return NULL;
}

/*
** py_flushSources()
**
** Params:   
** Returns: nothing
*/
PyObject *py_flushSources( PyObject *, PyObject *args )
{
  if (!gEngine)
  { 
    PyErr_SetString(PyExc_AssertionError, "Engine not initialized");
    return NULL;
  }
  gEngine->flushSources();
  return PyInt_FromLong(1);  
}


/*
** py_flushTextures()
**
** Params:   
** Returns: nothing
*/
PyObject *py_flushTextures( PyObject *, PyObject *args )
{
  if (!gEngine)
  { 
    PyErr_SetString(PyExc_AssertionError, "Engine not initialized");
    return NULL;
  }
  gEngine->flushTextures();
  return PyInt_FromLong(1);  
}


static PyMethodDef EngineFunctions[] =
{
  {"initialize",   py_initialize,   METH_VARARGS, "Initialize engine" },
  {"shutdown",     py_shutdown,     METH_VARARGS, "Initialize engine" },
  {"addObject",    py_addObject,    METH_VARARGS, "add graphics object" },
  {"removeObject", py_removeObject, METH_VARARGS, "remove graphics object" },
  {"render",       py_render,       METH_VARARGS, "render scene" },
  {"setView",      py_setView,      METH_VARARGS, "set viewport origin" },
  {"getWidth",     py_getWidth,     METH_VARARGS, "get screen width" },
  {"getHeight",    py_getHeight,    METH_VARARGS, "get screen height" },
  {"worldToScreen",py_worldToScreen,METH_VARARGS, "convert coordinates" },
  {"screenToWorld",py_screenToWorld,METH_VARARGS, "convert coordinates" },
  {"getSources",   py_getSources,   METH_VARARGS, "get sources" },
  {"getTextures",  py_getTextures,  METH_VARARGS, "get textures" },
  {"flushSources", py_flushSources, METH_VARARGS, "flush all sources" },
  {"flushTextures",py_flushTextures,METH_VARARGS, "flush all textures" },

  {"GraphicsObject", py_new_GraphicsObject,  METH_VARARGS, "create a graphics object" },
  {NULL,           NULL,            NULL,         NULL }
};


extern "C" __declspec(dllexport) void initcEngine()
{
  py_GraphicsObject_Type.ob_type = &PyType_Type;

  (void) Py_InitModule( "cEngine", EngineFunctions );
}



/*
def initialize(width, height):
def addObject(object, x, y, facing):
def removeObject(object):
def render():
def setView(posX, posY):
def getWidth():
def getHeight():
def worldToScreen(posX, posY):
def screenToWorld(posX, posY):
def getSources():
def getTextures():
def flushTextures():
def flushSources():
*/
