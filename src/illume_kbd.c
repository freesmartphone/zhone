#include <string.h>
#include <X11/Xlib.h>
#include <Ecore_X.h>
#include <Ecore_X_Atoms.h>

typedef enum {
        MTPRemoteNone = 0,
        MTPRemoteShow,
        MTPRemoteHide,
        MTPRemoteToggle,
} MTPRemoteOperation;

void illume_kbd_protocol_send_event(MTPRemoteOperation op)
{
  XEvent xev;
  memset(&xev, 0, sizeof(XEvent));

  Ecore_X_Display *disp;
  disp = ecore_x_display_get();

  xev.xclient.type = ClientMessage;
  xev.xclient.display = disp;
  xev.xclient.window = ecore_x_window_root_first_get();
  xev.xclient.message_type = ecore_x_atom_get("_MTP_IM_INVOKER_COMMAND");
  xev.xclient.format = 32;
  xev.xclient.data.l[0] = op;

  XSendEvent(disp,
             ecore_x_window_root_first_get(),
             False,
             SubstructureRedirectMask | SubstructureNotifyMask,
             &xev);

  XSync(ecore_x_display_get(), False);
}

void illume_kbd_show()
{
   illume_kbd_protocol_send_event(MTPRemoteShow);
}

void illume_kbd_hide()
{
   illume_kbd_protocol_send_event(MTPRemoteHide);
}

