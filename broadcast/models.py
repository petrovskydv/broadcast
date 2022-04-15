from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Mailing(models.Model):
    launch = models.DateTimeField('Дата и время запуска рассылки', db_index=True)
    end = models.DateTimeField('Дата и время окончания рассылки')
    text = models.TextField('Текст сообщения для доставки клиенту')
    mobile_operator_code = models.PositiveSmallIntegerField('Код мобильного оператора')
    tag = models.CharField('Тэг', max_length=20)

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

    def __str__(self):
        return f'{self.id} {self.launch}'


class Client(models.Model):
    phone_number = PhoneNumberField(
        'Номер телефона',
        help_text='В формате +7XXXXXXXXXX (X - цифра от 0 до 9)',
        unique=True
    )
    # TODO реализовать заполнение из номера
    mobile_operator_code = models.PositiveSmallIntegerField('Код мобильного оператора', db_index=True)
    tag = models.CharField('Тэг', max_length=20, db_index=True)
    time_zone = models.CharField('Часовой пояс', max_length=20)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.phone_number}'


class Message(models.Model):
    created_at = models.DateTimeField('Дата и время создания (отправки)', auto_now_add=True)
    status = models.BooleanField('Статус отправки', db_index=True)
    mailing = models.ForeignKey(
        Mailing,
        on_delete=models.PROTECT,
        related_name='messages',
        verbose_name='Рассылка'
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
        related_name='messages',
        verbose_name='Клиент'
    )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'{self.mailing.id} {self.client.id}'
