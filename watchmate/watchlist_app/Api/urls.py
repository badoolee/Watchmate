from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from watchlist_app.Api.views import movie_list, movie_details
from watchlist_app.Api.views import (
    MovieList,
    MovieDetails,
    StreamPlatformList,
    StreamPlatformDetails,
    ReviewList,
    ReviewDetails,
    ReviewCreate,
    StreamPlatformVS,
    UserReview,
    WatchListG,
)

router = DefaultRouter()
router.register("stream", StreamPlatformVS, basename="streamplatform")

urlpatterns = [
    path("list/", MovieList.as_view(), name="movie-list"),
    path("<int:pk>/", MovieDetails.as_view(), name="movie-details"),
    path("list2/", WatchListG.as_view(), name="watch-list"),
    path("", include(router.urls)),
    # path("stream/", StreamPlatformList.as_view(), name="streamplatform-list"),
    # path(
    #     "stream/<int:pk>",
    #     StreamPlatformDetails.as_view(),
    #     name="streamplatform-detail",
    # ),
    # path("review/", ReviewList.as_view(), name="review-list"),
    # path("review/<int:pk>", ReviewDetails.as_view(), name="review-details"),
    path("<int:pk>/review-create/", ReviewCreate.as_view(), name="review-create"),
    path("<int:pk>/review/", ReviewList.as_view(), name="review-list"),
    path("review/<int:pk>/", ReviewDetails.as_view(), name="review-details"),
    path("review/", UserReview.as_view(), name="user-review-details"),
]
