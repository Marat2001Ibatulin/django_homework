from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Advertisement, Favorite
from .filters import AdvertisementFilter
from .serializers import AdvertisementSerializer, FavoriteSerializer
from .permissions import IsOwnerOrAdminOrReadOnly
from django_filters import rest_framework as filters
from django.db.models import Q

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Advertisement.objects.filter(
                Q(draft='NO') | Q(creator=user)
            )
        else:
            return Advertisement.objects.filter(
                draft='NO'
            )

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AdvertisementFilter


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create",]:
            return [IsAuthenticated()]
        else:
            return [IsOwnerOrAdminOrReadOnly()]

class FavoriteViewSet(ModelViewSet):

    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Favorite.objects.filter(user=user)

    @action(
        detail=True,
        methods=['get'],
        url_path='toggle',
    )
    def favorite(self, request, pk):
        user = request.user
        adv_obj = Advertisement.objects.filter(id=pk)[0]
        if user == adv_obj.creator:
            raise ValidationError('Нельзя добавить свое объявление в избранное')
        favorite_obj, created = Favorite.objects.get_or_create(
            user=request.user, adv_id=pk
        )

        if created:
            return Response(
                {'message': 'Контент добавлен в избранное'},
                status=status.HTTP_201_CREATED
            )
        else:
            favorite_obj.delete()
            return Response(
                {'message': 'Контент удален из избранного'},
                status=status.HTTP_200_OK
            )







