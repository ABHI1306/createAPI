from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class CSRFExemptMixin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self,*args,**kwrgs):
        return super().dispatch(*args,**kwrgs)

    