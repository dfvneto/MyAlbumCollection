from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import AlbumCollection.routing


# pro0ject level routing
application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            AlbumCollection.routing.websocket_urlpatterns
        )
    ),
})
