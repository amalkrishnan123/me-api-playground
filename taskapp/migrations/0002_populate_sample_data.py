from django.db import migrations

def populate_data(apps, schema_editor):
    Profile = apps.get_model('taskapp', 'Profile')
    Skill = apps.get_model('taskapp', 'Skill')
    Project = apps.get_model('taskapp', 'Project')

    # Create Profile
    if not Profile.objects.exists():
        Profile.objects.create(
            name="John Doe",
            email="john@example.com",
            education="B.Sc. Computer Science"
        )

    # Create Skills
    python_skill, _ = Skill.objects.get_or_create(name="Python")
    django_skill, _ = Skill.objects.get_or_create(name="Django")
    react_skill, _ = Skill.objects.get_or_create(name="React")

    # Create Projects
    if not Project.objects.filter(title="E-Commerce API").exists():
        p1 = Project.objects.create(
            title="E-Commerce API",
            description="A fully functional REST API for an e-commerce platform.",
            link="https://github.com/example/ecommerce"
        )
        p1.skills.add(python_skill, django_skill)

    if not Project.objects.filter(title="Portfolio Frontend").exists():
        p2 = Project.objects.create(
            title="Portfolio Frontend",
            description="A modern, responsive portfolio website.",
            link="https://github.com/example/portfolio"
        )
        p2.skills.add(react_skill)

class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_data),
    ]
