from django.test import TestCase
from .models import Editor, Articles, tags
import datetime as dt
# Create your tests here.
class EditorTestClass(TestCase):
    #set up method
    def setUp(self):
        self.charity = Editor(first_name = 'Charity', last_name = 'Mutembei', email = 'charrykarimi0721263471@gmail.com')


    #test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.charity,Editor))

    #testing save method
    def test_save_method(self):
        self.charity.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
class ArticlesTestClass(TestCase):

    def setUp(self):
        #creating a new editor and saving it
        self.charity = Editor(first_name = 'Charity', last_name = 'Mutembei', email = 'charrykarimi0721263471')
        self.charity.save_editor()

        #creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()


        self.new_article = Articles(title = 'Test Article', post = 'This is a random test post', editor = self.charity)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Articles.objects.all().delete()
    def test_get_news_today(self):
        today_news = Articles.today_news()
        self.assertTrue(len(today_news)> 0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Articles.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
