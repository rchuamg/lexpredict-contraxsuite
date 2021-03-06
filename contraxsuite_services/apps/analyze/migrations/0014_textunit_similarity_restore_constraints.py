# Generated by Django 2.2.13 on 2020-06-29 09:30

from django.db import migrations, models
import django.db.models.deletion

from apps.analyze.similarity_textunit_migration_common import restore_textunitsim_constraints, \
    drop_textunitsim_constraints

TABLE_NAME = 'analyze_textunitsimilarity'

class Migration(migrations.Migration):
    dependencies = [
        ('analyze', '0013_vacuum_textunit_similarity'),
    ]

    operations = [
        migrations.RunPython(restore_textunitsim_constraints,
                             reverse_code=drop_textunitsim_constraints),
        migrations.AlterField(
            model_name='textunitsimilarity',
            name='document_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='similar_document_a_set', to='document.Document'),
        ),
        migrations.AlterField(
            model_name='textunitsimilarity',
            name='document_b',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='similar_document_b_set', to='document.Document'),
        ),
        migrations.AlterField(
            model_name='textunitsimilarity',
            name='project_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='similar_project_a_set', to='project.Project'),
        ),
        migrations.AlterField(
            model_name='textunitsimilarity',
            name='project_b',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='similar_project_b_set', to='project.Project'),
        ),
    ]
