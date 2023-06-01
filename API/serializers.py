from rest_framework import serializers
from django.contrib.auth.models import User
from data.models import Crypto
from articles.models import Article


class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = [
            "id",
            "name",
            "slug",
            "price",
            "total_supply",
            "market_cap",
            "volume_change_24h",
            "percent_change_24h",
            "user_favourite",
        ]


class UserSerializer(serializers.ModelSerializer):
    favourite = CryptoSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "favourite"]


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "name", "url"]
