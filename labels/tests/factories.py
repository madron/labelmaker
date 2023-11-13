import factory
from .. import models


class StyleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Style

    name = factory.Sequence(lambda n: 'style-{}'.format(n))


class LabelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Label

    name = factory.Sequence(lambda n: 'label-{}'.format(n))
    style = factory.SubFactory(StyleFactory)


class TemplateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Template

    name = factory.Sequence(lambda n: 'label-{}'.format(n))
