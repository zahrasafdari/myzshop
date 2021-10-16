from django.urls import path
from .views import add_user_order, remove_order_detail,user_open_order

urlpatterns = [
    path('add-user-order',add_user_order),
    path('user-open-order',user_open_order,name='user-open-order'),
    path('remove-order-detail/<detail_id>', remove_order_detail),

]