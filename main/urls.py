from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from apps.team.views import (
    TeamCreateView, 
    TeamDetail, 
    TeamListView
)

from apps.discounts.views import (
    PromotionList, 
    PromotionCreate,
    PromotionDetail, 
    CategoryList,
    CategoryCreate, 
    CategoryDetail,
    SubcategoryList,
    SubcategoryCreate,
    SubcategoryDetail, 
    ServiceList,
    ServiceCreate,
    ServiceDetail
)

from apps.otzyv.views import (
    ReviewList,
    ReviewCreate,
    ReviewDetail,
    ArticleList,
    ArticleCreate,
    ArticleDetail,
    ArticleImageCreate,
    ArticleImageDetail,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Beauty Day",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

team = [
    path('teamlist/', TeamListView.as_view()),
    path('teamecreate/', TeamCreateView.as_view()),
    path('team/<int:pk>/', TeamDetail.as_view()),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('team/', include(team)),
    path('gallery/', include('apps.team.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
 
    path('promotions/', PromotionList.as_view(), name='promotion_list'),
    path('promotions/create', PromotionCreate.as_view(), name='promotion_create'),
    path('promotions/<int:pk>/', PromotionDetail.as_view(), name='promotion_detail'),
    path('categories/', CategoryList.as_view(), name='category_list'),
    path('categories/create', CategoryCreate.as_view(), name='category_create'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    path('subcategories/', SubcategoryList.as_view(), name='subcategory_list'),
    path('subcategories/create', SubcategoryCreate.as_view(), name='subcategory_create'),
    path('subcategories/<int:pk>/', SubcategoryDetail.as_view(), name='subcategory_detail'),
    path('services/', ServiceList.as_view(), name='service_list'),
    path('services/create', ServiceCreate.as_view(), name='service_create'),
    path('services/<int:pk>/', ServiceDetail.as_view(), name='service_detail'),

    path('reviews/', ReviewList.as_view(), name='review-list'),
    path('review/', ReviewCreate.as_view(), name='review-create'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('articles/', ArticleList.as_view(), name='article_list'),
    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('articles/int:pk/', ArticleDetail.as_view(), name='article_detail'),
    path('article-images/create/', ArticleImageCreate.as_view(), name='image_create'),
    path('article-images/int:pk/', ArticleImageDetail.as_view(), name='image_detail'),
]


