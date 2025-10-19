from django.db import models

class Video(models.Model):
    GENRE_CHOICES = [
        ('Comedy', 'Comedy'),
        ('Romance', 'Romance'),
        ('Action', 'Action'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Animation', 'Animation'),
        ('Thriller', 'Thriller'),
        ('Other', 'Other'),
    ]

    movie_id = models.AutoField(primary_key=True, db_column='MovieID')
    title = models.CharField(max_length=200, db_column='MovieTitle')
    actor1 = models.CharField(max_length=100, db_column='Actor1Name')
    actor2 = models.CharField(max_length=100, blank=True, db_column='Actor2Name')
    director = models.CharField(max_length=100, db_column='DirectorName')
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, db_column='MovieGenre')
    release_year = models.PositiveIntegerField(db_column='ReleaseYear')

    class Meta:
        db_table = 'Video'
