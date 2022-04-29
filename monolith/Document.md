
# cloudProject

دیتاست این پروژه تاریخچه فروش بازی ها از سال  1980 تا 2020 بر روی پلتفرم های متفاوت است.

این پروژه متشکل از سرویس های زیر است:

- سرویس authentication:  که در این سرویس کاربر نام کاربری و رمز خود را وارد می کند و در جواب به او یک توکن داده می شود.

- سرویس game: در این سرویس کاربر می تواند تمامی اطلاعات مربوط به بازی را من جمله بدست آوردن بازی بر اساس رتبه، سال انتشار، نام و ژانر بدست آورد.

- سرویس analysis:  در این سرویس کاربر می تواند نمودار های مربوط به سرویس قبل را مشاهده کند.

 سرویس های authentication و analysis به شدت به سرویس game وابسته بودند و این موضوع باعث شد تا نمودار ها را از درخواست های اصلی جدا کنیم. 
 برای گرفتن پاسخ از بقیه سرویس ها لازم تا token ای به آن ها داده شود که این خود نشان دهنده وابستگی بقیه سرویس ها به سرویس authentication است.
 
 ![image](https://user-images.githubusercontent.com/46274547/165891059-ba880fc6-a8ae-4252-813f-c49815487e69.png)


![image](https://user-images.githubusercontent.com/46274547/165891122-2a2458be-596c-4387-9911-a59351fa62cc.png)



در تمامی سرویس ها token چک می شود.

## Authentication service
در این سرویس کاربر نام کاربری خود را با کلید username در body درخواست به صورت form data قرار می دهد.

`POST /api/user/sign_in/`

#### example:

body:

username:mohadese

respose:



## Game service

در این سرویس اطلاعات مربوط به بازی قرار دارد.


`GET /api/data_sales/search_by_platform/<paltform>/<pk>`

با استفاده از این api میتوان با اسم platform در بازی ها جستجو کرد و اطلاعات بازی ها را گرفت.



`GET /api/data_sales/search_by_rank/<rank>`

در این  api میتوان اطلاعات تمامی بازی هایی که rank آن ها برابر با رنک داده شده است گرفت.


`GET /api/data_sales/search_by_year/<year>/<pk>`

با استفاده از این api می توان تمامی بازی هایی که در سال خاصی منتشر شده اند را گرفت.


`GET /api/data_sales/search_by_genre/<genre>/<pk>`

با استفاده از این api میتوان تمامی بازی در ژانر خاصی را گرفت.


`GET /api/data_sales/all_data/`

با استفاده از این api میتوان تمامی بازی ها را گرفت.


## Analysis service

`/api/analyse_sales/compare_game/chart/<name>/<name>`

این api اسم دو بازی مختلف را میگیرد و با استفاده از اسم آن ها را مقایسه کرد و نموداری در قالب html درست می کند.

