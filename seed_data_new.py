import os
import sys
from datetime import datetime

from src.main import app, db
from src.models.product import Category, Product, Order
from src.models.content import Page, MenuItem
from src.models.user import User

def seed_data():
    with app.app_context():
        # Create tables
        db.create_all()

        # Clear existing data (optional, for fresh seeding)
        # It's important to delete in reverse order of foreign key dependencies
        db.session.query(Order).delete()
        db.session.query(Product).delete()
        db.session.query(Category).delete()
        db.session.query(Page).delete()
        db.session.query(MenuItem).delete()
        db.session.query(User).delete()
        db.session.commit()

        # Insert categories
        categories_data = [
            {"id": 1, "name": "Facebook Accounts", "description": "Various Facebook accounts with different specifications", "created_at": "2025-07-22T07:34:13.318482"},
            {"id": 2, "name": "Facebook Softregs", "description": "Soft registered Facebook accounts", "created_at": "2025-07-22T07:34:13.318485"},
            {"id": 3, "name": "Facebook With friends", "description": "Facebook accounts with existing friends", "created_at": "2025-07-22T07:34:13.318485"},
            {"id": 4, "name": "Facebook Aged", "description": "Aged Facebook accounts from different years", "created_at": "2025-07-22T07:34:13.318486"},
            {"id": 5, "name": "Facebook With friends and age", "description": "Aged Facebook accounts with friends", "created_at": "2025-07-22T07:34:13.318488"},
            {"id": 6, "name": "Facebook For advertising", "description": "Facebook accounts optimized for advertising", "created_at": "2025-07-22T07:34:13.318489"},
            {"id": 7, "name": "Gmail", "description": "", "created_at": "2025-07-22T07:46:13.910986"},
            {"id": 8, "name": "Linkedin", "description": "", "created_at": "2025-07-22T07:46:17.796262"},
            {"id": 9, "name": "Instagram", "description": "", "created_at": "2025-07-22T07:46:21.685545"},
            {"id": 10, "name": "Gvoice", "description": "", "created_at": "2025-07-22T07:46:25.370027"},
            {"id": 11, "name": "AT&T", "description": "", "created_at": "2025-07-22T07:46:29.035262"},
            {"id": 12, "name": "Outlook", "description": "", "created_at": "2025-07-22T07:46:32.336645"},
            {"id": 13, "name": "Craigslist", "description": "", "created_at": "2025-07-22T07:46:34.803639"},
            {"id": 14, "name": "Reddit", "description": "", "created_at": "2025-07-22T07:46:37.489375"},
            {"id": 15, "name": "Tiktok", "description": "", "created_at": "2025-07-22T07:46:40.926816"},
            {"id": 16, "name": "Gmx.com", "description": "", "created_at": "2025-07-22T07:46:43.562704"},
            {"id": 17, "name": "Grinder", "description": "", "created_at": "2025-07-22T07:46:46.736044"},
            {"id": 18, "name": "Snapchat", "description": "", "created_at": "2025-07-22T07:46:50.808307"},
            {"id": 19, "name": "Twitter", "description": "", "created_at": "2025-07-22T07:46:53.340341"},
            {"id": 20, "name": "Tinder", "description": "", "created_at": "2025-07-22T07:46:58.920638"},
            {"id": 21, "name": "Telegram", "description": "", "created_at": "2025-07-22T07:47:02.180643"},
            {"id": 22, "name": "Bumble", "description": "", "created_at": "2025-07-22T07:47:04.621178"},
            {"id": 23, "name": "Badoo", "description": "", "created_at": "2025-07-22T07:47:07.097569"},
            {"id": 24, "name": "Okcupid", "description": "", "created_at": "2025-07-22T07:47:10.596771"},
            {"id": 25, "name": "Apple", "description": "", "created_at": "2025-07-22T07:47:13.330273"},
            {"id": 26, "name": "Nextdoor", "description": "", "created_at": "2025-07-22T07:47:15.802788"},
            {"id": 27, "name": "BLK", "description": "", "created_at": "2025-07-22T07:47:18.227966"},
            {"id": 28, "name": "Meetme", "description": "", "created_at": "2025-07-22T07:47:23.154182"},
            {"id": 29, "name": "Dating", "description": "", "created_at": "2025-07-22T07:47:25.498872"}
        ]

        for item in categories_data:
            category = Category(
                id=item['id'],
                name=item['name'],
                description=item['description'],
                created_at=datetime.fromisoformat(item['created_at']) if item['created_at'] else None
            )
            db.session.add(category)
        db.session.commit()
        print(f"Inserted {len(categories_data)} categories.")

        # Insert products
        products_data = [
            {"id": 1, "name": "FB Accounts | Verified by e-mail, there is no email in the set. Male or female.", "description": "The account profiles may be empty or have limited entries such as photos and other information. 2FA included. Cookies are included. Accounts are registered in United Kingdom IP.", "price": 0.278, "stock": 384, "image_url": "/static/images/facebook-account.png", "category_id": 1, "created_at": "2025-07-22T07:34:13.323200", "updated_at": "2025-07-22T07:34:13.323203", "is_sold": False, "account_details": None},
            {"id": 2, "name": "FB Accounts | Verified by email (email not included). Male or female.", "description": "The account profiles may be empty or have limited entries such as photos and other information. 2FA included. Registered from USA IP.", "price": 0.296, "stock": 1679, "image_url": "/static/images/facebook-account.png", "category_id": 1, "created_at": "2025-07-22T07:34:13.324615", "updated_at": "2025-07-22T07:34:13.324618", "is_sold": False, "account_details": None},
            {"id": 3, "name": "FB Accounts | The number of subscribers is 50+. Verified by e-mail.", "description": "The account profiles may be empty or have limited entries such as photos and other information. 2FA in the set. Tokens are included in the package. Accounts are registered in Bangladesh IP.", "price": 0.999, "stock": 34, "image_url": "/static/images/facebook-account.png", "category_id": 3, "created_at": "2025-07-22T07:34:13.325515", "updated_at": "2025-07-22T07:34:13.325517", "is_sold": False, "account_details": None},
            {"id": 4, "name": "FB Accounts | [PVA] 100+ followers (friends and followers). Verified by email.", "description": "Email@gmail.com included. Female or male. Partially filled profiles. 2FA in the set. Registered from Bangladesh IP.", "price": 1.02, "stock": 153, "image_url": "/static/images/facebook-account.png", "category_id": 3, "created_at": "2025-07-22T07:34:13.326316", "updated_at": "2025-07-22T07:38:59.698621", "is_sold": False, "account_details": None},
            {"id": 5, "name": "FB Accounts | The accounts are registered 09.2024. Verified by e-mail.", "description": "There is no email in the set. Female or male. Partially filled profile. Registered from Bangladesh IP.", "price": 0.87, "stock": 3140, "image_url": "/static/images/facebook-account.png", "category_id": 4, "created_at": "2025-07-22T07:34:13.327083", "updated_at": "2025-07-22T07:34:13.327085", "is_sold": False, "account_details": None},
            {"id": 6, "name": "FB Accounts | The accounts were registered in 2020. Verified by email.", "description": "@rambler.ru (email included). Male or female. The profiles information is partially filled. Registered from Ukraine IP.", "price": 1.39, "stock": 110, "image_url": "/static/images/facebook-account.png", "category_id": 4, "created_at": "2025-07-22T07:34:13.327854", "updated_at": "2025-07-22T07:34:13.327856", "is_sold": False, "account_details": None},
            {"id": 7, "name": "FB Accounts | Activated 2 Business Managers, acceptable for ads. Verified by email.", "description": "Email NOT included. Male and female. Partially filled profile. Cookies are included in the set. Registered from Turkey IP.", "price": 2.78, "stock": 56, "image_url": "/static/images/facebook-account.png", "category_id": 6, "created_at": "2025-07-22T07:34:13.328549", "updated_at": "2025-07-22T07:34:13.328551", "is_sold": False, "account_details": None},
            {"id": 8, "name": "GMail Accounts | Verified by SMS. Phone number not included", "description": "Profile Security method. Registered from different countries IPs. High quality Gmail accounts verified by SMS with phone numbers not included.", "price": 0.5, "stock": 184, "image_url": "/static/images/gmail-account.png", "category_id": 7, "created_at": "2025-07-22T07:54:27.278882", "updated_at": "2025-07-22T07:54:27.278886", "is_sold": False, "account_details": None},
            {"id": 9, "name": "GMail Accounts | 1 Month Aged | Recovery Email Included", "description": "1 month aged Gmail accounts with recovery email included. Worldwide IPs registration. Perfect for various online activities.", "price": 0.6, "stock": 95, "image_url": "/static/images/gmail-account.png", "category_id": 7, "created_at": "2025-07-22T07:54:27.286570", "updated_at": "2025-07-22T07:54:27.286573", "is_sold": False, "account_details": None},
            {"id": 10, "name": "GMail Accounts | Registered in 6.2025. Additional email included", "description": "Fresh Gmail accounts registered in June 2025. Additional email included with password. Male or female. Registered from MIX IP.", "price": 0.65, "stock": 159, "image_url": "/static/images/gmail-account.png", "category_id": 7, "created_at": "2025-07-22T07:54:27.293511", "updated_at": "2025-07-22T07:54:27.293513", "is_sold": False, "account_details": None},
            {"id": 11, "name": "Facebook Accounts | Fresh Registered | Email Verified", "description": "Fresh Facebook accounts with email verification. Ready for immediate use. High quality profiles with basic information filled.", "price": 0.8, "stock": 120, "image_url": "/static/images/facebook-account.png", "category_id": 1, "created_at": "2025-07-22T07:54:27.300245", "updated_at": "2025-07-22T07:54:27.300248", "is_sold": False, "account_details": None},
            {"id": 12, "name": "Facebook Accounts | Phone Verified | USA IP", "description": "Phone verified Facebook accounts registered from USA IP addresses. Includes phone number and email access.", "price": 1.2, "stock": 85, "image_url": "/static/images/facebook-account.png", "category_id": 1, "created_at": "2025-07-22T07:54:27.306693", "updated_at": "2025-07-22T07:54:27.306696", "is_sold": False, "account_details": None},
            {"id": 13, "name": "Facebook Accounts | Business Manager Ready", "description": "Facebook accounts ready for Business Manager setup. Perfect for advertising and business purposes.", "price": 2.5, "stock": 45, "image_url": "/static/images/facebook-account.png", "category_id": 1, "created_at": "2025-07-22T07:54:27.313425", "updated_at": "2025-07-22T07:54:27.313428", "is_sold": False, "account_details": None},
            {"id": 14, "name": "Instagram Accounts | Fresh | Email Verified", "description": "Fresh Instagram accounts with email verification. Clean profiles ready for content creation and marketing.", "price": 0.9, "stock": 200, "image_url": "/static/images/instagram-account.png", "category_id": 9, "created_at": "2025-07-22T07:54:27.319309", "updated_at": "2025-07-22T07:54:27.319311", "is_sold": False, "account_details": None},
            {"id": 15, "name": "Instagram Accounts | Phone Verified | USA", "description": "Phone verified Instagram accounts from USA. Includes phone number access and email verification.", "price": 1.5, "stock": 150, "image_url": "/static/images/instagram-account.png", "category_id": 9, "created_at": "2025-07-22T07:54:27.325332", "updated_at": "2025-07-22T07:54:27.325334", "is_sold": False, "account_details": None},
            {"id": 16, "name": "Instagram Accounts | Aged 6 Months | Followers Included", "description": "6 months aged Instagram accounts with 100-500 followers. Perfect for influencer marketing and brand building.", "price": 3.0, "stock": 75, "image_url": "/static/images/instagram-account.png", "category_id": 9, "created_at": "2025-07-22T07:54:27.330793", "updated_at": "2025-07-22T07:54:27.330795", "is_sold": False, "account_details": None},
            {"id": 17, "name": "Twitter Accounts | Email Verified | Fresh", "description": "Fresh Twitter accounts with email verification. Ready for tweeting and social media marketing campaigns.", "price": 0.7, "stock": 180, "image_url": "/static/images/twitter-account.png", "category_id": 19, "created_at": "2025-07-22T07:54:27.336290", "updated_at": "2025-07-22T07:54:27.336293", "is_sold": False, "account_details": None},
            {"id": 18, "name": "Twitter Accounts | Phone Verified | USA IP", "description": "Phone verified Twitter accounts registered from USA IP addresses. High quality for business use.", "price": 1.3, "stock": 90, "image_url": "/static/images/twitter-account.png", "category_id": 19, "created_at": "2025-07-22T07:54:27.342375", "updated_at": "2025-07-22T07:54:27.342377", "is_sold": False, "account_details": None},
            {"id": 19, "name": "Twitter Accounts | Aged 3 Months | Followers", "description": "3 months aged Twitter accounts with 50-200 followers. Perfect for established social media presence.", "price": 2.8, "stock": 60, "image_url": "/static/images/twitter-account.png", "category_id": 19, "created_at": "2025-07-22T07:54:27.347383", "updated_at": "2025-07-22T07:54:27.347385", "is_sold": False, "account_details": None},
            {"id": 20, "name": "LinkedIn Accounts | Professional Profiles | Email Verified", "description": "Professional LinkedIn accounts with complete profiles. Email verified and ready for networking.", "price": 2.0, "stock": 100, "image_url": "/static/images/linkedin-account.png", "category_id": 8, "created_at": "2025-07-22T07:54:27.352099", "updated_at": "2025-07-22T07:54:27.352101", "is_sold": False, "account_details": None},
            {"id": 21, "name": "LinkedIn Accounts | Premium Features | USA", "description": "LinkedIn accounts with premium features enabled. Perfect for business networking and lead generation.", "price": 5.0, "stock": 40, "image_url": "/static/images/linkedin-account.png", "category_id": 8, "created_at": "2025-07-22T07:54:27.357064", "updated_at": "2025-07-22T07:54:27.357065", "is_sold": False, "account_details": None},
            {"id": 22, "name": "LinkedIn Accounts | Aged 1 Year | Connections", "description": "1 year aged LinkedIn accounts with 100+ connections. Established professional network included.", "price": 8.0, "stock": 25, "image_url": "/static/images/linkedin-account.png", "category_id": 8, "created_at": "2025-07-22T07:54:27.361672", "updated_at": "2025-07-22T07:54:27.361674", "is_sold": False, "account_details": None},
            {"id": 23, "name": "TikTok Accounts | Fresh | Email Verified", "description": "Fresh TikTok accounts with email verification. Ready for content creation and viral marketing.", "price": 1.0, "stock": 250, "image_url": "/static/images/tiktok-account.png", "category_id": 15, "created_at": "2025-07-22T07:54:27.367363", "updated_at": "2025-07-22T07:54:27.367365", "is_sold": False, "account_details": None},
            {"id": 24, "name": "TikTok Accounts | Phone Verified | USA", "description": "Phone verified TikTok accounts from USA. High quality for influencer marketing campaigns.", "price": 1.8, "stock": 120, "image_url": "/static/images/tiktok-account.png", "category_id": 15, "created_at": "2025-07-22T07:54:27.371966", "updated_at": "2025-07-22T07:54:27.371968", "is_sold": False, "account_details": None},
            {"id": 25, "name": "TikTok Accounts | Aged 2 Months | Followers", "description": "2 months aged TikTok accounts with 500-1000 followers. Perfect for established content creators.", "price": 4.5, "stock": 50, "image_url": "/static/images/tiktok-account.png", "category_id": 15, "created_at": "2025-07-22T07:54:27.376441", "updated_at": "2025-07-22T07:54:27.376443", "is_sold": False, "account_details": None},
            {"id": 26, "name": "Telegram Accounts | Phone Verified | Fresh", "description": "Fresh Telegram accounts with phone verification. Ready for messaging and channel management.", "price": 0.8, "stock": 300, "image_url": "/static/images/telegram-account.png", "category_id": 21, "created_at": "2025-07-22T07:54:27.380760", "updated_at": "2025-07-22T07:54:27.380762", "is_sold": False, "account_details": None},
            {"id": 27, "name": "Telegram Accounts | Premium Features | USA", "description": "Telegram accounts with premium features enabled. Perfect for business communication.", "price": 2.5, "stock": 80, "image_url": "/static/images/telegram-account.png", "category_id": 21, "created_at": "2025-07-22T07:54:27.385614", "updated_at": "2025-07-22T07:54:27.385615", "is_sold": False, "account_details": None},
            {"id": 28, "name": "Telegram Accounts | Aged 6 Months | Channels", "description": "6 months aged Telegram accounts with channel memberships. Established presence included.", "price": 3.5, "stock": 45, "image_url": "/static/images/telegram-account.png", "category_id": 21, "created_at": "2025-07-22T07:54:27.390221", "updated_at": "2025-07-22T07:54:27.390223", "is_sold": False, "account_details": None},
            {"id": 29, "name": "Snapchat Accounts | Email Verified | Fresh", "description": "Fresh Snapchat accounts with email verification. Ready for social media marketing and content sharing.", "price": 1.2, "stock": 150, "image_url": "/static/images/snapchat-account.png", "category_id": 18, "created_at": "2025-07-22T07:54:27.394751", "updated_at": "2025-07-22T07:54:27.394753", "is_sold": False, "account_details": None},
            {"id": 30, "name": "Snapchat Accounts | Phone Verified | USA", "description": "Phone verified Snapchat accounts from USA. High quality for influencer marketing.", "price": 2.0, "stock": 100, "image_url": "/static/images/snapchat-account.png", "category_id": 18, "created_at": "2025-07-22T07:54:27.399148", "updated_at": "2025-07-22T07:54:27.399150", "is_sold": False, "account_details": None},
            {"id": 31, "name": "Snapchat Accounts | Aged 3 Months | Friends", "description": "3 months aged Snapchat accounts with 50-100 friends. Perfect for established social presence.", "price": 3.8, "stock": 60, "image_url": "/static/images/snapchat-account.png", "category_id": 18, "created_at": "2025-07-22T07:54:27.403669", "updated_at": "2025-07-22T07:54:27.403670", "is_sold": False, "account_details": None},
            {"id": 32, "name": "Reddit Accounts | Email Verified | Fresh", "description": "Fresh Reddit accounts with email verification. Ready for community engagement and marketing.", "price": 0.6, "stock": 400, "image_url": "/static/images/reddit-account.png", "category_id": 14, "created_at": "2025-07-22T07:54:27.408259", "updated_at": "2025-07-22T07:54:27.408261", "is_sold": False, "account_details": None},
            {"id": 33, "name": "Reddit Accounts | Aged 1 Month | Karma", "description": "1 month aged Reddit accounts with 100+ karma points. Perfect for community participation.", "price": 1.5, "stock": 200, "image_url": "/static/images/reddit-account.png", "category_id": 14, "created_at": "2025-07-22T07:54:27.412674", "updated_at": "2025-07-22T07:54:27.412676", "is_sold": False, "account_details": None},
            {"id": 34, "name": "Reddit Accounts | High Karma | Aged 6 Months", "description": "6 months aged Reddit accounts with 1000+ karma. Established reputation for marketing.", "price": 5.0, "stock": 50, "image_url": "/static/images/reddit-account.png", "category_id": 14, "created_at": "2025-07-22T07:54:27.417236", "updated_at": "2025-07-22T07:54:27.417238", "is_sold": False, "account_details": None}
        ]

        for item in products_data:
            product = Product(
                id=item['id'],
                name=item['name'],
                description=item['description'],
                price=item['price'],
                stock=item['stock'],
                image_url=item['image_url'],
                category_id=item['category_id'],
                created_at=datetime.fromisoformat(item['created_at']) if item['created_at'] else None,
                updated_at=datetime.fromisoformat(item['updated_at']) if item['updated_at'] else None,
                account_details=item['account_details'],
                is_sold=item['is_sold']
            )
            db.session.add(product)
        db.session.commit()
        print(f"Inserted {len(products_data)} products.")

        # Insert pages
        pages_data = [
            {"id": 1, "title": "Frequently Asked Questions", "slug": "faq", "content": "# Frequently Asked Questions\n\n## What is AccsMarket?\nAccsMarket is your trusted marketplace for high-quality social media accounts.\n\n## How do I buy an account?\nBrowse our categories, select an account, proceed to checkout, and complete your purchase.\n\n## What payment methods are accepted?\nWe accept various payment methods including credit cards and cryptocurrencies.\n\n## Is my purchase secure?\nYes, all transactions are secured with the latest encryption technologies.\n\n## Can I get a refund?\nRefund policies vary by product. Please refer to our Terms of Use for details.", "meta_description": "Answers to common questions about AccsMarket and our services.", "meta_keywords": "FAQ, questions, support, help, AccsMarket", "is_published": True, "created_at": "2025-07-22T08:07:22.337793", "updated_at": "2025-07-22T08:07:22.337799"},
            {"id": 2, "title": "Terms of Use", "slug": "terms", "content": "# Terms of Use\n\n## 1. Acceptance of Terms\nBy accessing and using AccsMarket, you agree to be bound by these Terms of Use.\n\n## 2. Services Provided\nAccsMarket provides a platform for buying and selling social media accounts.\n\n## 3. User Responsibilities\nUsers are responsible for maintaining the confidentiality of their account information.\n\n## 4. Prohibited Activities\nAny illegal or unauthorized use of the platform is strictly prohibited.\n\n## 5. Limitation of Liability\nAccsMarket is not liable for any damages arising from the use of our services.\n\n## 6. Governing Law\nThese Terms shall be governed by and construed in accordance with the laws of the jurisdiction where AccsMarket operates.", "meta_description": "Legal terms and conditions for using the AccsMarket platform.", "meta_keywords": "terms, conditions, legal, use, policy", "is_published": True, "created_at": "2025-07-22T08:08:24.167644", "updated_at": "2025-07-22T08:08:24.167647"},
            {"id": 3, "title": "Useful Information", "slug": "useful-information", "content": "# Useful Information\n\n## Tips for Account Security\nAlways change passwords immediately after purchase. Enable two-factor authentication.\n\n## Understanding Account Types\nLearn about different types of accounts: aged, PVA, softregs, etc.\n\n## How to Contact Support\nFor any issues, please visit our Contact page or use the live chat feature.", "meta_description": "Helpful tips and information for users of AccsMarket.", "meta_keywords": "information, tips, guide, security, support", "is_published": True, "created_at": "2025-07-22T08:09:21.406291", "updated_at": "2025-07-22T08:09:21.406293"},
            {"id": 4, "title": "Rules", "slug": "rules", "content": "# Rules\n\n## 1. General Conduct\nUsers must conduct themselves respectfully and adhere to all platform guidelines.\n\n## 2. Prohibited Content\nPosting or sharing illegal, offensive, or harmful content is strictly forbidden.\n\n## 3. Account Usage\nAccounts purchased must be used in accordance with the terms of the respective social media platform.\n\n## 4. Reporting Violations\nReport any violations of these rules to our support team immediately.", "meta_description": "Rules and guidelines for using the AccsMarket platform.", "meta_keywords": "rules, guidelines, conduct, violations", "is_published": True, "created_at": "2025-07-22T08:10:19.173563", "updated_at": "2025-07-22T08:10:19.173565"},
            {"id": 5, "title": "Become a Seller", "slug": "become-seller", "content": "# Become a Seller\n\n## Join Our Network\nAre you interested in selling social media accounts? Join our growing network of trusted sellers.\n\n## Requirements\nSellers must meet certain quality and reliability standards. Contact us for more details.\n\n## How to Apply\nFill out the seller application form on our website or contact our partnership team.", "meta_description": "Information on how to become a seller on AccsMarket.", "meta_keywords": "seller, sell accounts, partnership, apply", "is_published": True, "created_at": "2025-07-22T08:11:22.717254", "updated_at": "2025-07-22T08:11:22.717257"},
            {"id": 6, "title": "Privacy Policy", "slug": "privacy-policy", "content": "# Privacy Policy\n\n## 1. Data Collection\nWe collect personal information to provide and improve our services.\n\n## 2. Use of Data\nYour data is used to process transactions, provide support, and personalize your experience.\n\n## 3. Data Security\nWe implement robust security measures to protect your personal information.\n\n## 4. Third-Party Disclosure\nWe do not sell or trade your personally identifiable information to outside parties.\n\n## 5. Your Rights\nYou have the right to access, modify, or delete your personal data.", "meta_description": "Our commitment to protecting your privacy and personal data.", "meta_keywords": "privacy, policy, data, security, GDPR", "is_published": True, "created_at": "2025-07-22T08:12:21.356895", "updated_at": "2025-07-22T08:12:21.356898"},
            {"id": 7, "title": "About Us", "slug": "about", "content": "# About AccsMarket\n\n## Our Mission\nAccsMarket aims to be the leading marketplace for secure and reliable social media accounts.\n\n## Our Team\nWe are a dedicated team of professionals committed to providing the best service.\n\n## Our Values\nIntegrity, security, and customer satisfaction are at the core of everything we do.", "meta_description": "Learn more about AccsMarket, our mission, and our team.", "meta_keywords": "about us, mission, team, values", "is_published": True, "created_at": "2025-07-22T08:13:20.126797", "updated_at": "2025-07-22T08:13:20.126799"},
            {"id": 8, "title": "Contact Us", "slug": "contact", "content": "# Contact Us\n\n## Get in Touch\nHave questions or need support? We\\'re here to help.\n\n## Support Channels\n- **Email**: support@accsmarket.com\n- **Live Chat**: Available 24/7 on our website\n- **Phone**: +123 456 7890\n\n## Business Inquiries\nFor partnerships and business proposals, please email business@accsmarket.com.", "meta_description": "How to contact AccsMarket for support, inquiries, and partnerships.", "meta_keywords": "contact, support, email, phone, live chat", "is_published": True, "created_at": "2025-07-22T08:14:17.554914", "updated_at": "2025-07-22T08:14:17.554916"}
        ]

        for item in pages_data:
            page = Page(
                id=item['id'],
                title=item['title'],
                slug=item['slug'],
                content=item['content'],
                meta_description=item['meta_description'],
                meta_keywords=item['meta_keywords'],
                is_published=item['is_published'],
                created_at=datetime.fromisoformat(item['created_at']) if item['created_at'] else None,
                updated_at=datetime.fromisoformat(item['updated_at']) if item['updated_at'] else None
            )
            db.session.add(page)
        db.session.commit()
        print(f"Inserted {len(pages_data)} pages.")

        # Insert orders
        orders_data = [
            {"id": 1, "customer_name": "John Doe", "customer_email": "john.doe@example.com", "product_id": 4, "quantity": 1, "total_price": 1.02, "status": "completed", "payment_method": "crypto", "created_at": "2025-07-22T07:38:59.701291", "updated_at": "2025-07-22T07:38:59.701293", "account_details": None}
        ]

        for item in orders_data:
            order = Order(
                id=item['id'],
                product_id=item['product_id'],
                customer_email=item['customer_email'],
                customer_name=item['customer_name'],
                quantity=item['quantity'],
                total_price=item['total_price'],
                status=item['status'],
                payment_method=item['payment_method'],
                account_details=item['account_details'],
                created_at=datetime.fromisoformat(item['created_at']) if item['created_at'] else None,
                updated_at=datetime.fromisoformat(item['updated_at']) if item['updated_at'] else None
            )
            db.session.add(order)
        db.session.commit()
        print(f"Inserted {len(orders_data)} orders.")

        print("Seed data created successfully!")

if __name__ == '__main__':
    seed_data()

