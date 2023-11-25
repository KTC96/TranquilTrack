from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mood_tracker', '0008_diary_mood_diary_sleep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievements',
            name='achievement_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='achievements',
            name='achievement_user',
            field=models.ForeignKey(default='001', on_delete=django.db.models.deletion.CASCADE, related_name='achievements', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='diary',
            name='owner',
            field=models.ForeignKey(default='001', on_delete=django.db.models.deletion.CASCADE, related_name='diaries', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='diary',
            name='mood',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='diary',
            name='sleep',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]
