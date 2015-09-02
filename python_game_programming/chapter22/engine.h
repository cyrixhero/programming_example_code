#include <stdlib.h>

#include <list>

using namespace std;

class GraphicsObject
{
 public:
  GraphicsObject(const char *source, bool mobile, const char *image = NULL);
  ~GraphicsObject();

  void getSimData(float &centerX, float &centerY, float &width, float &height);
  void setState(float x, float y, float facing);
  void setFrame(int frame);
  void nextFrame();
  void destroy();

 protected:

  bool m_mobile;
  const char *m_source;
  const char *m_image;
};


class GraphicsEngine
{
 public:

  GraphicsEngine(int width, int height); 
  ~GraphicsEngine();

  bool addObject(GraphicsObject *object, float x, float y, float facing);
  bool removeObject(GraphicsObject *object);
  void render();
  void setView(int x, int y);
  int getWidth();
  int getHeight();
  void worldToScreen(const float inX, const float inY, float &outX, float &outY);
  void screenToWorld(const float inX, const float inY, float &outX, float &outY);
  void flushTextures();
  void flushSources();

 protected:

  int m_width;
  int m_height;
  int m_viewPosX;
  int m_viewPosY;

  list<GraphicsObject*> m_objects;
  
};
