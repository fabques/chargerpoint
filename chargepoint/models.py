from django.db import models
from django.utils.translation import gettext as _
from model_utils.models import TimeStampedModel, StatusModel
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE


class ChargePoint(SafeDeleteModel,TimeStampedModel,StatusModel):

    # Safe delete policy
    _safedelete_policy = SOFT_DELETE_CASCADE

    # Status choices definition
    STATUS_CREATED = 'READY'
    STATUS_CHARGING = 'CHARGING'
    STATUS_WAITING = 'WAITING'
    STATUS_ERROR = 'ERROR'

    STATUS = [
        (STATUS_CREATED, _('Punto de carga creado')),
        (STATUS_CHARGING, _('Punto de carga eliminado')),
        (STATUS_WAITING, _('Punto de carga esperando ')),
        (STATUS_ERROR, _('Error en punto de carga')),
    ]

    # Model fields definition
    name = models.CharField(_('Nombre'), max_length=32, unique=True)
