#include "engine.h"

GraphicsObject::GraphicsObject(const char *source, bool mobile, const char *image) :
  m_mobile(mobile),
  m_source(source),
  m_image(image)
{
}

GraphicsObject::~GraphicsObject()
{
}


GraphicsEngine::GraphicsEngine(int width, int height) :
  m_width(width),
  m_height(height),
  m_viewPosX(0),
  m_viewPosY(0)
{
}

GraphicsEngine::~GraphicsEngine()
{
}


bool GraphicsEngine::addObject(GraphicsObject *object, float x, float y, float facing)
{
  printf("Engine adding Object %d\n", object);
  return true;
}

bool GraphicsEngine::removeObject(GraphicsObject *object)
{
  printf("Engine removing Object %d\n", object);
  return true;
}

void GraphicsEngine::render()
{
}

void GraphicsEngine::setView(int x, int y)
{
}

int GraphicsEngine::getWidth()
{
  return 0;
}

int GraphicsEngine::getHeight()
{
  return 0;
}

void GraphicsEngine::worldToScreen(const float inX, const float inY, float &outX, float &outY)
{
  outX = 0;
  outY = 0;
}

void GraphicsEngine::screenToWorld(const float inX, const float inY, float &outX, float &outY)
{
  outX = 0;
  outY = 0;
}

void GraphicsEngine::flushTextures()
{
}

void GraphicsEngine::flushSources()
{
}

