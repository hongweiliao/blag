import logging
import time
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from back_web.models import Admin

log = logging.getLogger(__name__)


class LoginStatusMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path in ['/admin/login/'] or '/web/' in request.path:
            return None
        user_id = request.session.get('user_id')
        if user_id:
            user = Admin.objects.get(pk=user_id)
            request.user = user
            return None
        else:
            return HttpResponseRedirect(reverse('admin:login'))


class LogMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        # 绑定在request上一个属性,表示访问的时间
        request.init_time = time.time()

    def process_response(self, request, response):
        # 请求url耗时
        count_time = time.time() - request.init_time
        # 状态码
        code = response.status_code
        # 请求地址
        path = request.path
        # 请求方法
        method = request.method
        # 相应内容
        content = response.content
        log_str = '%s %s %s %s %s' % (path, method, code, count_time, content)
        # 交给logger处理日志
        log.info(log_str)
        return response

