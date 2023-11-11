from rest_framework import serializers
from .models import Curso, Avaliacao

class AvaliacaoSerializers(serializers.ModelSerializer):

    class Meta:
        # email so será exibido quando alguem for fazer um cadastro
        extra_kwargs = {
            'email' : {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'publicacao',
            'ativo',
        )


class CursoSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'atualizacao',
            'ativo',
        )