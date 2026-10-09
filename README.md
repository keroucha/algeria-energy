# موقع الطاقات المتجددة في الجزائر (Python / Flask)

## ماذا يفعل؟
1. يدخل الزائر **اللغة** و**البريد الإلكتروني**.
2. يصلك **إيميل** يخبرك أن شخصاً جديداً دخل (ويُحفظ الزائر أيضاً في `visitors.db`).
3. يرى الزائر **أحدث أخبار الطاقات المتجددة في الجزائر** بلغته، تُجلب تلقائياً من Google News وتُحدَّث كل 30 دقيقة.

## التشغيل محلياً
```bash
python -m venv venv
source venv/bin/activate        # على ويندوز: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # ثم عدّل القيم داخله
python app.py                   # افتح http://127.0.0.1:5000
```

## إعداد الإيميل (Gmail)
1. فعّل التحقق بخطوتين في حساب Google.
2. أنشئ **App Password** من https://myaccount.google.com/apppasswords
3. ضعه في `SMTP_PASSWORD`، وضع بريدك في `SMTP_USER` و`OWNER_EMAIL`.

> إن لم تضبط SMTP يعمل الموقع بشكل طبيعي لكن لن تصلك الإيميلات (يظهر تحذير في السجل).

## النشر
على أي استضافة بايثن (Render, Railway, PythonAnywhere, VPS):
```bash
gunicorn app:app
```
واضبط متغيرات `.env` من لوحة الاستضافة. تذكّر: خطط الاستضافة المجانية قد تمسح `visitors.db` عند إعادة التشغيل، لكن الإيميلات تبقى عندك.

## هيكل الملفات
| الملف | الدور |
|---|---|
| `app.py` | المسارات والتحقق والحماية |
| `mailer.py` | إرسال إشعار الزائر الجديد |
| `news.py` | جلب الأخبار مع تخزين مؤقت |
| `db.py` | حفظ الزوار في SQLite |
| `i18n.py` | النصوص بالعربية/الفرنسية/الإنجليزية |
| `templates/`, `static/` | الواجهة |
