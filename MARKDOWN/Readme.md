Wallet project

MODELS:

Created models by importing user to create one to one relationship between wallet and user

OneToOneField is used to specify the wallet instance has a relationship with a single user instance

On_delete is used to specify if related user instance is detected then the wallet instance will also be deleted .

User,balance and is_active are the three fields of model class.

SERIALIZER:
 
 The meta class within the walletserializer is to provide metadata to the serializer

 Model attribute specifies the model that this serializer is associated with

 Fields attribute specify the fields should be included in serialization output.

 VIEWS:

 Viewset named walletviewset is responsible for CRUD operations

 serializer_class is used to specify the serializer class that should be used for serializing and serializing wallet instances

 permission_classes specify permisions that should be checked before allowing access to the viewset,it allows access only to the authenticated users.

 get_queyset() is used to retrive wallet instances,here it returns only wallet instances that are associated with the current authenticated user.

 perform_create() specifies the actions that should be taken when a new wallet instance is created.

 views sets the user field of the newly created wallet instance to the current authenticated user.

 URLs:

 Include and path are used to define the URL patterns in Django

 Routers create a router object that will automatically generate URL patterns for the views associated with the registered viewset

 walletviewset from wallet_app.views is a custom viewset class that defines the behaviour of the views that will be registered with the router.

 Create a router object by calling the DefaultRouter()

 Register the walletviewset with the router by calling the register()method on router object

 Associates the views defined in walletviewset with the URL pattern '/wallet/'

 Define URL patterns in which first path object maps the root URL to the router.urls, this means any request to the root URL will be handled by the views associated with the registered viewset and the second path maps the URL'/api_auth/' to the 'rest_framework.urls' namespace which provides default views for handling user authentication.

 It sets up a REST Api for the wallet model in the wallet_app using walletviewset to define the behaviour of the views

