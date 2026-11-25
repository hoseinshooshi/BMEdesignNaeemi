# BMEdesignNaeemi

## استفاده از پروژه

1. پکیج‌ها را نصب کنید:

   ```bash
   pip install -r requirements.txt
   ```

2. فایل‌های دیتاست ANSUR II را در پوشه `data/` قرار دهید. نام فایل‌ها باید دقیقاً این‌ها باشد:
   - `ANSUR II FEMALE Public.csv`
   - `ANSUR II MALE Public.csv`

   اگر فایل‌ها را ندارید، اسکریپت زیر را اجرا کنید:

   ```bash
   python scripts/download_ansur.py
   ```

   برای دریافت مجدد و جایگزینی فایل‌های موجود:

   ```bash
   python scripts/download_ansur.py --force
   ```

3. اندازه‌های نمونه را در ابتدای تابع `main` در فایل `examples/design_example.py` و در دیکشنری `base` تغییر دهید. ورودی از کاربر پرسیده نمی‌شود؛ اندازه‌ها از همان بخش کد خوانده می‌شوند.

4. اجرای طراحی و تخمین:

   ```bash
   python examples/design_example.py
   ```

   فایل‌های خروجی STL و تصویر مدل در پوشه `output/` ذخیره می‌شوند.

## دیتاست

- صفحه رسمی معرفی دیتاست و متغیرها: https://ph.health.mil/topics/workplacehealth/ergo/Pages/Anthropometric-Database.aspx
- دریافت دیتاست از Penn State OPEN Design Lab: https://www.openlab.psu.edu/ansur2/
- نسخه CSV مورد استفاده اسکریپت دانلود: https://github.com/senihberkay/US-Army-ANSUR-II


## الگوریتم ماشین لرنینگ

برای تخمین **محیط مچ دست (wristcircumference، میلی‌متر)** از الگوریتم **Random Forest Regressor** کتابخانه scikit-learn استفاده شده است.

- ویژگی‌های ورودی مدل: طول دست (`handlength`)، عرض دست (`handbreadth`) و محیط ساعد در حالت خمیده (`forearmcircumferenceflexed`).
- خروجی مدل: محیط مچ دست (`wristcircumference`).
- تنظیمات اصلی: ۵۰۰ درخت، `min_samples_leaf=3` و `random_state=42`.
- داده‌ها به‌صورت تصادفی به بخش آموزش و آزمون (۸۰/۲۰) تقسیم می‌شوند. MAE، RMSE و R² بخش آزمون هنگام اجرا چاپ می‌شوند.
- مقدار پیش‌بینی‌شده محیط مچ، همراه اندازه‌های تعریف‌شده در `base`، به ورودی طراحی ارتز داده می‌شود.

**نکته:** ANSUR II نماینده تمام جمعیت‌ها نیست. معیارهای آزمون تصادفی به‌تنهایی دقت روی جمعیت هدف یا اعتبار بالینی را ثابت نمی‌کنند؛ مدل باید با داده‌های مستقل و متناسب با کاربران هدف ارزیابی شود.
