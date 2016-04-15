# coding=utf-8
import json

import mako.lookup
import mako.template
import tornado.httpserver
import tornado.ioloop
import tornado.web
import logging

logger = logging.getLogger('boilerplate.' + __name__)


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        template_path = self.get_template_path()
        self.lookup = mako.lookup.TemplateLookup(directories=[template_path], input_encoding='utf-8',
                                                 output_encoding='utf-8')

    def render_string(self, template_path, **kwargs):

        try:
            _debug = self.get_argument("debug", "false")
            template = self.lookup.get_template(template_path)
            namespace = self.get_template_namespace()
            namespace.update(kwargs)

            # siteConfig=WebConfig()
            env_kwargs = dict(
                handler=self,
                request=self.request,
                locale=self.locale,
                static_url=self.static_url,
                xsrf_form_html=self.xsrf_form_html,
                reverse_url=self.application.reverse_url,
                user_agent=self.request.headers["User-Agent"]

            )
            env_kwargs.update(kwargs)
            return template.render(**env_kwargs)
        except Exception as e:
            print("服务端错误")
            print(e)

    def write_json(self, obj, cls=None, **kwargs):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.finish(json.dumps(obj, cls=cls, **kwargs))

    def get_current_user(self):
        return self.get_secure_cookie("userName")

    def load_json(self):
        """Load JSON from the request body and store them in
        self.request.arguments, like Tornado does by default for POSTed form
        parameters.
        If JSON cannot be decoded, raises an HTTPError with status 400.
        """
        try:
            self.request.arguments = json.loads(self.request.body)
        except ValueError:
            msg = "Could not decode JSON: %s" % self.request.body
            logger.debug(msg)
            raise tornado.web.HTTPError(400, msg)

    def get_json_argument(self, name, default=None):
        """Find and return the argument with key 'name' from JSON request data.
        Similar to Tornado's get_argument() method.
        """
        if default is None:
            default = self._ARG_DEFAULT
        if not self.request.arguments:
            self.load_json()
        if name not in self.request.arguments:
            if default is self._ARG_DEFAULT:
                msg = "Missing argument '%s'" % name
                logger.debug(msg)
                raise tornado.web.HTTPError(400, msg)
            logger.debug("Returning default argument %s, as we couldn't find "
                         "'%s' in %s" % (default, name, self.request.arguments))
            return default
        arg = self.request.arguments[name]
        logger.debug("Found '%s': %s in JSON arguments" % (name, arg))
        return arg
