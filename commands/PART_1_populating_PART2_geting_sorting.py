# PART_1_populating

from django.contrib.auth.models import User
from author.models import Author
from category.models import Category
from post.models import Posts
from django.utils.text import slugify
from comment.models import Comments
from rating.models import Rating


user1 = User.objects.create_user(username="John", password="Johnpassword", email="lennon@ya.ru")
user2 = User.objects.create_user(username="Paul", password="Paulpassword", email="macarthy@ya.ru")


author1 = Author.objects.create(author_name='Jonny', user_id=user1)
author2 = Author.objects.create(author_name='Polly', user_id=user2)


cat1 = Category.objects.create(name='Music')
cat2 = Category.objects.create(name='Obituaries')
cat3 = Category.objects.create(name='Sports')
cat4 = Category.objects.create(name='Urgent_news')


post1 = Posts.objects.create(blog_type='News',
    title='John resurrected.',
    body='Vanity Fair has come up with an interesting although possibly not entirely successful  new angle on the approaching 70th anniversary of John Lennons birth. "Lennon at 70!" says the "web exclusive"  we dont doubt it  by David Kamp. "As he approaches the big milestone and his highly anticipated reunion dates with the Plastic Ono Band, the irrepressible ex-Beatle talks about cows, survival, and Yoko." Thats right. Theyve interviewed him, from the standpoint that he survived the fatal 1980 shooting and is about to go on tour again. Not only that, he got divorced from Yoko Ono in 1983, the Beatles reunited to perform at Live Aid ("Queen mopped the floor with us") and recorded a 1987 album called, er ... Everest. It was around the time of the Aids-themed Day in the Life re-release  "I read the news today, oh boy/ About a wave of boys who died too soon/ They wove a quilt out of their grief/ Its someones life you rob/ When you dont sheathe your knob" that Monkey lost the will to read. Whatever gets you through the night, eh?',
    author=author2)
post2 = Posts.objects.create(blog_type='Article',
    title='Paul died.',
    body=' Paul is Dead («Пол мертв», также известный как «PID») — история о предполагаемой смерти Пола Маккартни в 1966 году, циркулирующая в музыкальном мире с 1969 года. Ходят слухи, что Пол Маккартни разбил свою машину ранним утром в среду, 9 ноября 1966 года, после того, как покинул студию звукозаписи EMI в подавленном настроении. [ 1 ] Говорят, что его заменил двойник по имени Уильям Кэмпбелл, которого те, кто верит слухам, также называют Фаулом (сокращение от False Paul , что означает «Ложный Пол») .',
    slug=slugify('My-First-Post'),
    author=author1)
post3 = Posts.objects.create(blog_type='Article',
    title='Цой жив.',
    body='Сегодня Виктору Цою исполнилось бы 60. Он трагически погиб в 28, но успел стать героем целого поколения. Пожалуй, ни у кого из наших звезд не было и нет столько фанатов и подражателей. Почему он превратился в идола и за что мы его любим — в материале РИА Новости.',
    author=author1)

post4 = Posts.objects.create(blog_type='Article',
    title='My 4rd Post for testing preview',
    body='«Полнолуние и ретроградный Меркурий. Как это может повлиять на ваше праздничное настроение и привычки?»: Последнее полнолуние года принесет сегодня конец ретроградному Меркурию. «Предстоящее полнолуние — часть сочетания довольно значительных небесных событий. Не хочется драматизировать, но на какое-то время ситуация может стать странной, и если вы в последнее время чувствуете себя немного не в своей тарелке, на то есть веские причины. Декабрьское полнолуние часто называют Холодной луной — это ирокезское название, потому что с этого момента холодная погода по-настоящему начинает овладевать нами. Это время также известно как «Луна долгой ночи» из-за близости к зимнему солнцестоянию, которое отмечает самую длинную ночь в году. Предстоит также редчайшее событие — большое луностояние — когда наш спутник восходит и заходит в самых крайних точках горизонта, а также поднимается до самой высокой и самой низкой точки неба, что случается только раз в 18,6 года. С восходом холодной Луны закончится и ретроградный Меркурий»',
    author=author2)

post4.post_like()
post4.post_like()
post4.post_like()
post4.post_like()
post4.post_like()
post4.post_like()
post4.post_like()
post4.post_like()
post4.post_like()

post2.post_like()
post2.post_like()
post2.post_like()
post2.post_like()
post2.post_like()
post3.post_like()
post3.post_like()
post3.post_like()
post3.post_like()



categories_to_add = Category.objects.filter(name__in=["cat1", "cat4"])
post1.categories.add(*categories_to_add)
post1.save()

categories_to_add1 = Category.objects.filter(name__in=["cat1", "cat2"])
post2.categories.add(*categories_to_add1)
post2.save()

categories_to_add1 = Category.objects.filter(name__in=["cat1", "cat2"])
post3.categories.add(*categories_to_add1)
post3.save()

post1.post_like()
post1.post_like()
post1.post_like()



post2.post_dislike()
post2.post_dislike()
post2.post_dislike()




comment1 = Comments.objects.create(
    post=post1,  
    body="This is a test comment No1",
    author=author1
)

comment1.comment_like()
comment1.comment_like()
comment1.comment_like()

comment2 = Comments.objects.create(
    post=post2,  
    body="This is a test comment No2",
    author=author2
)

comment2.comment_dislike()
comment2.comment_dislike()
comment2.comment_dislike()

comment3 = Comments.objects.create(
    post=post3,  
    body="This is a test comment No3",
    author=author2
)

comment4 = Comments.objects.create(
    post=post4,  
    body="This is a test comment No4",
    author=author1
)

comment4.comment_like()
comment4.comment_like()
comment4.comment_like()
comment4.comment_like()
comment4.comment_like()
comment4.comment_like()
comment4.comment_like()
comment4.comment_like()
comment4.comment_like()

print(f"Пост comment4 теперь имеет {comment4.comment_rating} лайков.")



print(f"Пост '{post1.title}' теперь имеет {post1.post_rating} лайков.")



# PART_2_getting and sorting






from django.contrib.auth.models import User
from author.models import Author
from category.models import Category
from post.models import Posts
from django.utils.text import slugify
from comment.models import Comments
from rating.models import Rating


user1 = User.objects.get(pk=1)
user2 = User.objects.get(pk=2)

author1 = Author.objects.get(pk=1)
author2 = Author.objects.get(pk=2)


cat1 = Category.objects.get(pk=1)
cat2 = Category.objects.get(pk=2)
cat3 = Category.objects.get(pk=3)
cat4 = Category.objects.get(pk=4)

post1 = Posts.objects.get(pk=1)
post2 = Posts.objects.get(pk=2)
post3 = Posts.objects.get(pk=3)
post4 = Posts.objects.get(pk=4)

comment1 = Comments.objects.get(pk=1)
comment2 = Comments.objects.get(pk=2)
comment3 = Comments.objects.get(pk=3)
comment4 = Comments.objects.get(pk=4)

rating1 = Rating.objects.get_or_create(author=author1)
rating2 = Rating.objects.get_or_create(author=author2)

rating1.update_rating()
rating2.update_rating()

highest_rating = Rating.objects.order_by('-total_rating').select_related('author').first()
if highest_rating:
    print(f"Name: {highest_rating.author.author_name}, Highest Rating: {highest_rating.total_rating}")




best_post = Posts.objects.order_by('-post_rating').select_related('author').first()

if best_post:
    print(f"Date: {best_post.date}")
    print(f"Author: {best_post.author.author_name}")
    print(f"Post Rating: {best_post.post_rating}")
    print(f"Title: {best_post.title}")
    print(f"Body: {best_post.preview}")
else:
    print("No posts found.")

Date: 2024-12-16 18:37:44.229055+00:00
Author: Polly
Post Rating: 9
Title: My 4rd Post for testing preview
Body: «Полнолуние и ретроградный Меркурий. Как это может повлиять на ваше праздничное настроение и привычки?»: Последнее полнолуни...

post_with_comments = Posts.objects.filter(title='My 4rd Post for testing preview').select_related('author').first()

if post_with_comments:
    print(f"Post Title: {post_with_comments.title}")
    print(f"Post Date: {post_with_comments.date}")
    print(f"Post Author: {post_with_comments.author.author_name}")
    print(f"Post Rating: {post_with_comments.post_rating}")
    print(f"Post Preview: {post_with_comments.preview}")

    
    post_comments = Comments.objects.filter(post=post_with_comments).select_related('author')

    if post_comments.exists():
        print("\nComments for this post:")
        for comment in post_comments:
            print(f"Date: {comment.date}")
            print(f"User: {comment.author.author_name}")
            print(f"Comment Rating: {comment.comment_rating}")
            print(f"Text: {comment.body}")
            print("-" * 40)  
    else:
        print("No comments found for this post.")
else:
    print("Post with the given title not found.")

Post Title: My 4rd Post for testing preview
Post Date: 2024-12-16 18:37:44.229055+00:00
Post Author: Polly
Post Rating: 9
Post Preview: «Полнолуние и ретроградный Меркурий. Как это может повлиять на ваше праздничное настроение и привычки?»: Последнее полнолуни...
Comments for this post:
Date: 2024-12-16 18:44:01.015568+00:00
User: Jonny
Comment Rating: 18
Text: This is a test comment No4