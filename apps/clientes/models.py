from django.db import models


class Cliente(models.Model):
    '''
    Customer entity used for sales, stock and relationship operations.
    '''

    nome: str = models.CharField(max_length=150)
    cpf_cnpj: str | None = models.CharField(max_length=18, blank=True, null=True)

    telefone: str | None = models.CharField(max_length=20, blank=True, null=True)
    email: str | None = models.EmailField(blank=True, null=True)

    cep: str | None = models.CharField(max_length=9, blank=True, null=True)
    endereco: str | None = models.CharField(max_length=200, blank=True, null=True)
    numero: str | None = models.CharField(max_length=10, blank=True, null=True)
    bairro: str | None = models.CharField(max_length=100, blank=True, null=True)
    cidade: str | None = models.CharField(max_length=100, blank=True, null=True)
    estado: str | None = models.CharField(max_length=2, blank=True, null=True)

    ativo: bool = models.BooleanField(default=True)

    criado_em: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    atualizado_em: models.DateTimeField = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nome

    class Meta:
        db_table = 'clientes'
        ordering = ['nome']
