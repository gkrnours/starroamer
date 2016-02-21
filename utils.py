import pickle
from functools import wraps
from flask import request, session, render_template
from oauth2client.client import Storage

def templated(template=None):
    """Allow a flask route to return a dict that would be used to render a
    template. The template location is either provided when using the decorator
    or computed from the route endpoint."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            template_name = template
            if template_name is None:
                template_name = "%s.html" % request.endpoint.replace('.', '/')
            ctx = f(*args, **kwargs) or {}
            if not isinstance(ctx, dict):
                return ctx
            return render_template(template_name, **ctx)
        return decorated_function
    return decorator

class SessionCredStorage(Storage):
    """Take a credential object and store it into the session."""
    def locked_put(self, cred):
        session['_cred'] = pickle.dumps(cred)

    def locked_get(self):
        return pickle.loads(session.get('_cred'))
