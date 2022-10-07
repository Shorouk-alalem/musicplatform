 from artists.models import Artist
 from albums.models import Album
 1- Query: Create All artists
   * A1=Artist(stage_name="Ed Shereen",social_link_field="https://www.instgram.com/adele")
   * A1.save()
   * A2=Artist(stage_name="Adele",social_link_field="https://www.instgram.com/teddysphotos") 
   * A2.save()
   * A3=Artist(stage_name="Monir",social_link_field="https://www.instgram.com/mouniroffical")
   * A3.save()
   * A4=Artist(stage_name="CairoKee", social_link_field="https://www.instgram.com/amir.eid")
   * A4.save()
   * A5=Artist(stage_name="Asalah",social_link_field="https://www.instgram.com/asala")
   * A5.save()
2- Query: list down all artists 
   * Artist.objects.all() 
   Result of query:
   * <QuerySet [<Artist: Adele>, <Artist: Asalah>, <Artist: CairoKee>, <Artist: Ed Shereen>, <Artist: Monir>]>
3- Query: list down all artists sorted by name
   * Artist.objects.all().order_by('stage_name') 
   Result of Query:
   * <QuerySet [<Artist: Adele>, <Artist: Asalah>, <Artist: CairoKee>, <Artist: Ed Shereen>, <Artist: Monir>]>
   Note: the result of this query is the same as the previous query as I have set the defult order to be by name
4- Query: list down all artists whose name starts with `a`
   * Artist.objects.filter(stage_name__startswith="a")
   Result of Query:
   * <QuerySet [<Artist: Adele>, <Artist: Asalah>]>
5- Query: create some albums and assign them to any artist
   * Album1=Album(artist_name=Artist.objects.get(stage_name="Asalah"),name="bnt akaber" , creation_datetime=datetime.datetime(2022,3,2,12,13),release_datetime=datetime.datetime(2022,3,30,12,13),cost=400000)
   * Album1.save()
   * from django.utils import timezone
   * Album2=Album(artist_name=Artist.objects.get(stage_name="Asalah"),name="Ana" , creation_datetime=datetime.datetime(2022,3,2,12,13),release_datetime=timezone.now(),cost=40000)  
   * Album2.save()
   * Album3=Album(artist_name=Artist.objects.get(stage_name="CairoKee"),name="Layla" , creation_datetime=datetime.datetime(2022,5,2,12,13),release_datetime=datetime.datetime(2022,12,13,1,2),cost=50120)
   * Album3.save()
   * Album4=Album(artist_name=Artist.objects.get(stage_name="Ed Shereen"),name="perfect" , creation_datetime=datetime.datetime(2022,7,2,12,13),release_datetime=datetime.datetime(2022,8,2,1,2),cost=507700)
   * Album4.save()
   * Album5=Album(name="Younis" , creation_datetime=datetime.datetime(2022,2,2,12,13),release_datetime=datetime.datetime(2022,3,2,1,2),cost=40500)
   * art=Artist.objects.get(stage_name="Monir")
   * Album5.artist_name=art
   * Album5.save()
5- Query: get the latest released album
   * Album.objects.latest('release_datetime')
   Result of the query:
   * <Album: Layla>
6- Query: get all albums released before today
   *  Album.objects.filter(release_datetime__lt=datetime.date.today()) 
   Result of the Query:
   * <QuerySet [<Album: bnt akaber>, <Album: perfect>, <Album: Younis>]>
7- get all albums released today or before but not after today
   * Album.objects.filter(release_datetime__date__lte=datetime.date.today())
   Result of the Query:
   * <QuerySet [<Album: bnt akaber>, <Album: Ana>, <Album: perfect>, <Album: Younis>]>
8- count the total number of albums
   * Album.objects.count()
   Result of the query:
   * 5
9-  for each artist, list down all of his/her albums
    Query:
   * Album.objects.values('artist_name','name').order_by('artist_name','name')
    Result of query:
   * <QuerySet [{'artist_name': 5, 'name': 'Ana'}, {'artist_name': 5, 'name': 'bnt akaber'}, {'artist_name': 4, 'name': 'Layla'}, {'artist_name': 1, 'name': 'perfect'}, {'artist_name': 3, 'name': 'Younis'}]>
10- list down all albums ordered by cost then by name
   * AlbumsData=Album.objects.all().order_by('cost','name')
   * AlbumsData
   To show the result name with the cost : 
   * for i in AlbumsData:     
        print(i.name)
        print(i.cost)
   Result of the query:
   * <QuerySet [<Album: Ana>, <Album: Younis>, <Album: Layla>, <Album: bnt akaber>, <Album: perfect>]>









