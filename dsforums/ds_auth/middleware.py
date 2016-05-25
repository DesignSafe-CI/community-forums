from django.conf import settings
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from requests.exceptions import RequestException, HTTPError
import logging

logger = logging.getLogger(__name__)


class AgaveTokenRefreshMiddleware(object):

    def process_request(self, request):
        if request.path != '/logout/' and request.user.is_authenticated():
            try:
                token = request.user.agave_oauth
                if token and token.expired:
                    try:
                        token.refresh()
                    except HTTPError:
                        logger.exception('Agave Token refresh failed. Forcing logout',
                                         extra={'user': request.user.username})
                        logout(request)
            except ObjectDoesNotExist:
                logger.warn('Agave Token missing. Forcing logout.',
                            extra={'user': request.user.username})
                logout(request)
            except RequestException:
                logger.exception('Agave Token refresh failed. Forcing logout',
                                 extra={'user': request.user.username})
                logout(request)
