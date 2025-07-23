PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE user (
	id INTEGER NOT NULL, 
	username VARCHAR(80) NOT NULL, 
	email VARCHAR(120) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	UNIQUE (email)
);
CREATE TABLE category (
	id INTEGER NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	description TEXT, 
	created_at DATETIME, 
	PRIMARY KEY (id), 
	UNIQUE (name)
);
INSERT INTO category VALUES(1,'Facebook Accounts','Various Facebook accounts with different specifications','2025-07-22 07:34:13.318482');
INSERT INTO category VALUES(2,'Facebook Softregs','Soft registered Facebook accounts','2025-07-22 07:34:13.318485');
INSERT INTO category VALUES(3,'Facebook With friends','Facebook accounts with existing friends','2025-07-22 07:34:13.318485');
INSERT INTO category VALUES(4,'Facebook Aged','Aged Facebook accounts from different years','2025-07-22 07:34:13.318486');
INSERT INTO category VALUES(5,'Facebook With friends and age','Aged Facebook accounts with friends','2025-07-22 07:34:13.318488');
INSERT INTO category VALUES(6,'Facebook For advertising','Facebook accounts optimized for advertising','2025-07-22 07:34:13.318489');
INSERT INTO category VALUES(7,'Gmail','','2025-07-22 07:46:13.910986');
INSERT INTO category VALUES(8,'Linkedin','','2025-07-22 07:46:17.796262');
INSERT INTO category VALUES(9,'Instagram','','2025-07-22 07:46:21.685545');
INSERT INTO category VALUES(10,'Gvoice','','2025-07-22 07:46:25.370027');
INSERT INTO category VALUES(11,'AT&T','','2025-07-22 07:46:29.035262');
INSERT INTO category VALUES(12,'Outlook','','2025-07-22 07:46:32.336645');
INSERT INTO category VALUES(13,'Craigslist','','2025-07-22 07:46:34.803639');
INSERT INTO category VALUES(14,'Reddit','','2025-07-22 07:46:37.489375');
INSERT INTO category VALUES(15,'Tiktok','','2025-07-22 07:46:40.926816');
INSERT INTO category VALUES(16,'Gmx.com','','2025-07-22 07:46:43.562704');
INSERT INTO category VALUES(17,'Grinder','','2025-07-22 07:46:46.736044');
INSERT INTO category VALUES(18,'Snapchat','','2025-07-22 07:46:50.808307');
INSERT INTO category VALUES(19,'Twitter','','2025-07-22 07:46:53.340341');
INSERT INTO category VALUES(20,'Tinder','','2025-07-22 07:46:58.920638');
INSERT INTO category VALUES(21,'Telegram','','2025-07-22 07:47:02.180643');
INSERT INTO category VALUES(22,'Bumble','','2025-07-22 07:47:04.621178');
INSERT INTO category VALUES(23,'Badoo','','2025-07-22 07:47:07.097569');
INSERT INTO category VALUES(24,'Okcupid','','2025-07-22 07:47:10.596771');
INSERT INTO category VALUES(25,'Apple','','2025-07-22 07:47:13.330273');
INSERT INTO category VALUES(26,'Nextdoor','','2025-07-22 07:47:15.802788');
INSERT INTO category VALUES(27,'BLK','','2025-07-22 07:47:18.227966');
INSERT INTO category VALUES(28,'Meetme','','2025-07-22 07:47:23.154182');
INSERT INTO category VALUES(29,'Dating','','2025-07-22 07:47:25.498872');
CREATE TABLE pages (
	id INTEGER NOT NULL, 
	title VARCHAR(200) NOT NULL, 
	slug VARCHAR(100) NOT NULL, 
	content TEXT NOT NULL, 
	meta_description VARCHAR(300), 
	meta_keywords VARCHAR(300), 
	is_published BOOLEAN, 
	created_at DATETIME, 
	updated_at DATETIME, 
	PRIMARY KEY (id), 
	UNIQUE (slug)
);
INSERT INTO pages VALUES(1,'Frequently Asked Questions','faq',replace('# Frequently Asked Questions\n\n## What is AccsMarket?\nAccsMarket is your trusted marketplace for high-quality social media accounts.\n\n## How do I buy an account?\nBrowse our categories, select an account, proceed to checkout, and complete your purchase.\n\n## What payment methods are accepted?\nWe accept various payment methods including credit cards and cryptocurrencies.\n\n## Is my purchase secure?\nYes, all transactions are secured with the latest encryption technologies.\n\n## Can I get a refund?\nRefund policies vary by product. Please refer to our Terms of Use for details.','\n',char(10)),'Answers to common questions about AccsMarket and our services.','FAQ, questions, support, help, AccsMarket',1,'2025-07-22 08:07:22.337793','2025-07-22 08:07:22.337799');
INSERT INTO pages VALUES(2,'Terms of Use','terms',replace('# Terms of Use\n\n## 1. Acceptance of Terms\nBy accessing and using AccsMarket, you agree to be bound by these Terms of Use.\n\n## 2. Services Provided\nAccsMarket provides a platform for buying and selling social media accounts.\n\n## 3. User Responsibilities\nUsers are responsible for maintaining the confidentiality of their account information.\n\n## 4. Prohibited Activities\nAny illegal or unauthorized use of the platform is strictly prohibited.\n\n## 5. Limitation of Liability\nAccsMarket is not liable for any damages arising from the use of our services.\n\n## 6. Governing Law\nThese Terms shall be governed by and construed in accordance with the laws of the jurisdiction where AccsMarket operates.','\n',char(10)),'Legal terms and conditions for using the AccsMarket platform.','terms, conditions, legal, use, policy',1,'2025-07-22 08:08:24.167644','2025-07-22 08:08:24.167647');
INSERT INTO pages VALUES(3,'Useful Information','useful-information',replace('# Useful Information\n\n## Tips for Account Security\nAlways change passwords immediately after purchase. Enable two-factor authentication.\n\n## Understanding Account Types\nLearn about different types of accounts: aged, PVA, softregs, etc.\n\n## How to Contact Support\nFor any issues, please visit our Contact page or use the live chat feature.','\n',char(10)),'Helpful tips and information for users of AccsMarket.','information, tips, guide, security, support',1,'2025-07-22 08:09:21.406291','2025-07-22 08:09:21.406293');
INSERT INTO pages VALUES(4,'Rules','rules',replace('# Rules\n\n## 1. General Conduct\nUsers must conduct themselves respectfully and adhere to all platform guidelines.\n\n## 2. Prohibited Content\nPosting or sharing illegal, offensive, or harmful content is strictly forbidden.\n\n## 3. Account Usage\nAccounts purchased must be used in accordance with the terms of the respective social media platform.\n\n## 4. Reporting Violations\nReport any violations of these rules to our support team immediately.','\n',char(10)),'Rules and guidelines for using the AccsMarket platform.','rules, guidelines, conduct, violations',1,'2025-07-22 08:10:19.173563','2025-07-22 08:10:19.173565');
INSERT INTO pages VALUES(5,'Become a Seller','become-seller',replace('# Become a Seller\n\n## Join Our Network\nAre you interested in selling social media accounts? Join our growing network of trusted sellers.\n\n## Requirements\nSellers must meet certain quality and reliability standards. Contact us for more details.\n\n## How to Apply\nFill out the seller application form on our website or contact our partnership team.','\n',char(10)),'Information on how to become a seller on AccsMarket.','seller, sell accounts, partnership, apply',1,'2025-07-22 08:11:22.717254','2025-07-22 08:11:22.717257');
INSERT INTO pages VALUES(6,'Privacy Policy','privacy-policy',replace('# Privacy Policy\n\n## 1. Data Collection\nWe collect personal information to provide and improve our services.\n\n## 2. Use of Data\nYour data is used to process transactions, provide support, and personalize your experience.\n\n## 3. Data Security\nWe implement robust security measures to protect your personal information.\n\n## 4. Third-Party Disclosure\nWe do not sell or trade your personally identifiable information to outside parties.\n\n## 5. Your Rights\nYou have the right to access, modify, or delete your personal data.','\n',char(10)),'Our commitment to protecting your privacy and personal data.','privacy, policy, data, security, GDPR',1,'2025-07-22 08:12:21.356895','2025-07-22 08:12:21.356898');
INSERT INTO pages VALUES(7,'About Us','about',replace('# About AccsMarket\n\n## Our Mission\nAccsMarket aims to be the leading marketplace for secure and reliable social media accounts.\n\n## Our Team\nWe are a dedicated team of professionals committed to providing the best service.\n\n## Our Values\nIntegrity, security, and customer satisfaction are at the core of everything we do.','\n',char(10)),'Learn more about AccsMarket, our mission, and our team.','about us, mission, team, values',1,'2025-07-22 08:13:20.126797','2025-07-22 08:13:20.126799');
INSERT INTO pages VALUES(8,'Contact Us','contact',replace('# Contact Us\n\n## Get in Touch\nHave questions or need support? We\''re here to help.\n\n## Support Channels\n- **Email**: support@accsmarket.com\n- **Live Chat**: Available 24/7 on our website\n- **Phone**: +123 456 7890\n\n## Business Inquiries\nFor partnerships and business proposals, please email business@accsmarket.com.','\n',char(10)),'How to contact AccsMarket for support, inquiries, and partnerships.','contact, support, email, phone, live chat',1,'2025-07-22 08:14:17.554914','2025-07-22 08:14:17.554916');
CREATE TABLE menu_items (
	id INTEGER NOT NULL, 
	title VARCHAR(100) NOT NULL, 
	url VARCHAR(200) NOT NULL, 
	menu_type VARCHAR(50) NOT NULL, 
	order_index INTEGER, 
	is_active BOOLEAN, 
	target_blank BOOLEAN, 
	created_at DATETIME, 
	PRIMARY KEY (id)
);
CREATE TABLE homepage_section (
	id INTEGER NOT NULL, 
	section_type VARCHAR(50) NOT NULL, 
	title VARCHAR(200), 
	content TEXT, 
	order_index INTEGER, 
	is_active BOOLEAN, 
	css_classes VARCHAR(500), 
	background_color VARCHAR(20), 
	text_color VARCHAR(20), 
	image_url VARCHAR(500), 
	button_text VARCHAR(100), 
	button_url VARCHAR(500), 
	created_at DATETIME, 
	updated_at DATETIME, 
	PRIMARY KEY (id)
);
INSERT INTO homepage_section VALUES(1,'hero','Welcome to AccsMarket','Your trusted marketplace for social media accounts',4,1,NULL,'#1f2937','#ffffff',NULL,'Browse Accounts','#products','2025-07-23 01:25:54.911197','2025-07-23 01:41:32.762926');
INSERT INTO homepage_section VALUES(2,'product_categories','Available Account Categories','Browse our wide selection of verified social media accounts',1,1,NULL,NULL,NULL,NULL,NULL,NULL,'2025-07-23 01:25:54.911201','2025-07-23 01:41:32.760193');
INSERT INTO homepage_section VALUES(3,'info_block','WHAT TO ASK BEFORE BUYING ACCOUNTS',replace('Regarding Social Media (SOMIA), it is evident that this is an effective and one of the most potent means capable of pitching in almost every business industry and market. Presently all the marketers use Social Media as a platform for steering customers. There are some difficulties you can meet when choosing the right Social Media sites for marketing purposes. It won''t be confusing if you initially define the Social Media requirements that are to be used and choose the right supplier of Social Media accounts.\n\n**- Where most of the target audiences are?**\n\nIt is essential to determine where the target audiences are spending their time. This could be Instagram or Facebook or Twitter, whatever, but the thing is that purchased accounts with followers are to be profitable in marketing.\n\n**- Where is the activity of accounts reflected?**\n\nThe inactive accounts of Social Media are useless, even if they are accessible and well promoted. It is recommended to buy only active accounts.\n\n**- What are the search results of followers?**\n\nTry to determine what the users are searching for on SOMIA. This will bring you closer to profit.\n\n**- What Social Media meets your niche better than others?**\n\nIt is worth considering that you may not get leads from Social Media used by other business owners. Therefore, choose the Social Media sites that correspond to your niche.','\n',char(10)),2,1,NULL,'#ffffff','#374151',NULL,NULL,NULL,'2025-07-23 01:25:54.911202','2025-07-23 01:41:32.761535');
INSERT INTO homepage_section VALUES(4,'footer','© 2024 AccsMarket. All rights reserved.',replace('© 2024 AccsMarket. All rights reserved.\n','\n',char(10)),3,1,'','#ffffff','#374151','','','','2025-07-23 01:40:28.280612','2025-07-23 01:41:32.762344');
INSERT INTO homepage_section VALUES(5,'header','','',0,1,'','#ffffff','#374151','','','','2025-07-23 02:06:39.544358','2025-07-23 02:06:39.544363');
INSERT INTO homepage_section VALUES(6,'custom','','',2,1,'','#ffffff','#374151','','','','2025-07-23 02:11:28.248944','2025-07-23 02:11:28.248946');
INSERT INTO homepage_section VALUES(7,'custom','Featured Products','',5,1,'','#ffffff','#374151','','','','2025-07-23 02:34:36.991400','2025-07-23 02:34:36.991403');
CREATE TABLE site_settings (
	id INTEGER NOT NULL, 
	setting_key VARCHAR(100) NOT NULL, 
	setting_value TEXT, 
	setting_type VARCHAR(20), 
	description VARCHAR(500), 
	created_at DATETIME, 
	updated_at DATETIME, 
	PRIMARY KEY (id), 
	UNIQUE (setting_key)
);
INSERT INTO site_settings VALUES(1,'site_title','AccsMarket - Buy Social Media Accounts','text','Main site title displayed in browser tab','2025-07-23 01:25:54.912685','2025-07-23 01:25:54.912688');
INSERT INTO site_settings VALUES(2,'site_description','Your trusted marketplace for verified social media accounts','text','Site description for SEO','2025-07-23 01:25:54.912688','2025-07-23 01:25:54.912689');
INSERT INTO site_settings VALUES(3,'header_logo_text','ACCSmarketot','text','Logo text displayed in header','2025-07-23 01:25:54.912689','2025-07-23 02:04:49.492345');
INSERT INTO site_settings VALUES(4,'header_logo_subtext','duarduar.com','text','Logo subtext displayed in header','2025-07-23 01:25:54.912690','2025-07-23 02:05:02.214365');
INSERT INTO site_settings VALUES(5,'footer_copyright',replace('© 2024 AccsMarket. All rights reserved.\n© 2024 AccsMarket. All rights reserved.\n© 2024 AccsMarket. All rights reserved.\n© 2024 AccsMarket. All rights reserved.\n© 2024 AccsMarket. All rights reserved.\n','\n',char(10)),'text','Copyright text in footer','2025-07-23 01:25:54.912691','2025-07-23 01:40:11.952216');
INSERT INTO site_settings VALUES(6,'contact_email','support@accsmarket.com','text','Contact email address','2025-07-23 01:25:54.912691','2025-07-23 01:25:54.912692');
INSERT INTO site_settings VALUES(7,'enable_search','true','boolean','Enable/disable search functionality','2025-07-23 01:25:54.912692','2025-07-23 01:25:54.912693');
INSERT INTO site_settings VALUES(8,'products_per_page','20','number','Number of products to display per page','2025-07-23 01:25:54.912693','2025-07-23 01:25:54.912693');
CREATE TABLE product (
	id INTEGER NOT NULL, 
	name VARCHAR(200) NOT NULL, 
	description TEXT, 
	price FLOAT NOT NULL, 
	stock INTEGER, 
	image_url VARCHAR(500), 
	category_id INTEGER NOT NULL, 
	created_at DATETIME, 
	updated_at DATETIME, 
	account_details TEXT, 
	is_sold BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(category_id) REFERENCES category (id)
);
INSERT INTO product VALUES(1,'FB Accounts | Verified by e-mail, there is no email in the set. Male or female.','The account profiles may be empty or have limited entries such as photos and other information. 2FA included. Cookies are included. Accounts are registered in United Kingdom IP.',0.27800000000000002486,384,'/static/images/facebook-account.png',1,'2025-07-22 07:34:13.323200','2025-07-22 07:34:13.323203','{"type": "facebook_account", "verification": "email_verified", "includes": ["cookies", "2fa", "profile_data"]}',0);
INSERT INTO product VALUES(2,'FB Accounts | Verified by email (email not included). Male or female.','The account profiles may be empty or have limited entries such as photos and other information. 2FA included. Registered from USA IP.',0.29599999999999998534,1679,'/static/images/facebook-account.png',1,'2025-07-22 07:34:13.324615','2025-07-22 07:34:13.324618','{"type": "facebook_account", "verification": "email_verified", "includes": ["cookies", "2fa", "profile_data"]}',0);
INSERT INTO product VALUES(3,'FB Accounts | The number of subscribers is 50+. Verified by e-mail.','The account profiles may be empty or have limited entries such as photos and other information. 2FA in the set. Tokens are included in the package. Accounts are registered in Bangladesh IP.',0.99899999999999999911,34,'/static/images/facebook-account.png',3,'2025-07-22 07:34:13.325515','2025-07-22 07:34:13.325517','{"type": "facebook_account", "verification": "email_verified", "includes": ["cookies", "2fa", "profile_data"]}',0);
INSERT INTO product VALUES(4,'FB Accounts | [PVA] 100+ followers (friends and followers). Verified by email.','Email@gmail.com included. Female or male. Partially filled profiles. 2FA in the set. Registered from Bangladesh IP.',1.0200000000000000177,153,'/static/images/facebook-account.png',3,'2025-07-22 07:34:13.326316','2025-07-22 07:38:59.698621','{"type": "facebook_account", "verification": "email_verified", "includes": ["cookies", "2fa", "profile_data"]}',0);
INSERT INTO product VALUES(5,'FB Accounts | The accounts are registered 09.2024. Verified by e-mail.','There is no email in the set. Female or male. Partially filled profile. Registered from Bangladesh IP.',0.86999999999999999555,3140,'/static/images/facebook-account.png',4,'2025-07-22 07:34:13.327083','2025-07-22 07:34:13.327085','{"type": "facebook_account", "verification": "email_verified", "includes": ["cookies", "2fa", "profile_data"]}',0);
INSERT INTO product VALUES(6,'FB Accounts | The accounts were registered in 2020. Verified by email.','@rambler.ru (email included). Male or female. The profiles information is partially filled. Registered from Ukraine IP.',1.3899999999999999023,110,'/static/images/facebook-account.png',4,'2025-07-22 07:34:13.327854','2025-07-22 07:34:13.327856','{"type": "facebook_account", "verification": "email_verified", "includes": ["cookies", "2fa", "profile_data"]}',0);
INSERT INTO product VALUES(7,'FB Accounts | Activated 2 Business Managers, acceptable for ads. Verified by email.','Email NOT included. Male and female. Partially filled profile. Cookies are included in the set. Registered from Turkey IP.',2.7799999999999998046,56,'/static/images/facebook-account.png',6,'2025-07-22 07:34:13.328549','2025-07-22 07:34:13.328551','{"type": "facebook_account", "verification": "email_verified", "includes": ["cookies", "2fa", "profile_data"]}',0);
INSERT INTO product VALUES(8,'GMail Accounts | Verified by SMS. Phone number not included','Profile Security method. Registered from different countries IPs. High quality Gmail accounts verified by SMS with phone numbers not included.',0.5,184,'/static/images/gmail-account.png',7,'2025-07-22 07:54:27.278882','2025-07-22 07:54:27.278886','{"type": "gmail_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(9,'GMail Accounts | 1 Month Aged | Recovery Email Included','1 month aged Gmail accounts with recovery email included. Worldwide IPs registration. Perfect for various online activities.',0.59999999999999997779,95,'/static/images/gmail-account.png',7,'2025-07-22 07:54:27.286570','2025-07-22 07:54:27.286573','{"type": "gmail_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(10,'GMail Accounts | Registered in 6.2025. Additional email included','Fresh Gmail accounts registered in June 2025. Additional email included with password. Male or female. Registered from MIX IP.',0.6500000000000000222,159,'/static/images/gmail-account.png',7,'2025-07-22 07:54:27.293511','2025-07-22 07:54:27.293513','{"type": "gmail_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(11,'Facebook Accounts | Fresh Registered | Email Verified','Fresh Facebook accounts with email verification. Ready for immediate use. High quality profiles with basic information filled.',0.8000000000000000444,120,'/static/images/facebook-account.png',1,'2025-07-22 07:54:27.300245','2025-07-22 07:54:27.300248','{"type": "facebook_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(12,'Facebook Accounts | Phone Verified | USA IP','Phone verified Facebook accounts registered from USA IP addresses. Includes phone number and email access.',1.1999999999999999555,85,'/static/images/facebook-account.png',1,'2025-07-22 07:54:27.306693','2025-07-22 07:54:27.306696','{"type": "facebook_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(13,'Facebook Accounts | Business Manager Ready','Facebook accounts ready for Business Manager setup. Perfect for advertising and business purposes.',2.5,45,'/static/images/facebook-account.png',1,'2025-07-22 07:54:27.313425','2025-07-22 07:54:27.313428','{"type": "facebook_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(14,'Instagram Accounts | Fresh | Email Verified','Fresh Instagram accounts with email verification. Clean profiles ready for content creation and marketing.',0.9000000000000000222,200,'/static/images/instagram-account.png',9,'2025-07-22 07:54:27.319309','2025-07-22 07:54:27.319311','{"type": "instagram_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(15,'Instagram Accounts | Phone Verified | USA','Phone verified Instagram accounts from USA. Includes phone number access and email verification.',1.5,150,'/static/images/instagram-account.png',9,'2025-07-22 07:54:27.325332','2025-07-22 07:54:27.325334','{"type": "instagram_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(16,'Instagram Accounts | Aged 6 Months | Followers Included','6 months aged Instagram accounts with 100-500 followers. Perfect for influencer marketing and brand building.',3.0,75,'/static/images/instagram-account.png',9,'2025-07-22 07:54:27.330793','2025-07-22 07:54:27.330795','{"type": "instagram_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(17,'Twitter Accounts | Email Verified | Fresh','Fresh Twitter accounts with email verification. Ready for tweeting and social media marketing campaigns.',0.69999999999999995559,180,'/static/images/twitter-account.png',19,'2025-07-22 07:54:27.336290','2025-07-22 07:54:27.336293','{"type": "twitter_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(18,'Twitter Accounts | Phone Verified | USA IP','Phone verified Twitter accounts registered from USA IP addresses. High quality for business use.',1.3000000000000000444,90,'/static/images/twitter-account.png',19,'2025-07-22 07:54:27.342375','2025-07-22 07:54:27.342377','{"type": "twitter_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(19,'Twitter Accounts | Aged 3 Months | Followers','3 months aged Twitter accounts with 50-200 followers. Perfect for established social media presence.',2.7999999999999998223,60,'/static/images/twitter-account.png',19,'2025-07-22 07:54:27.347383','2025-07-22 07:54:27.347385','{"type": "twitter_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(20,'LinkedIn Accounts | Professional Profiles | Email Verified','Professional LinkedIn accounts with complete profiles. Email verified and ready for networking.',2.0,100,'/static/images/linkedin-account.png',8,'2025-07-22 07:54:27.352099','2025-07-22 07:54:27.352101','{"type": "linkedin_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(21,'LinkedIn Accounts | Premium Features | USA','LinkedIn accounts with premium features enabled. Perfect for business networking and lead generation.',5.0,40,'/static/images/linkedin-account.png',8,'2025-07-22 07:54:27.357064','2025-07-22 07:54:27.357065','{"type": "linkedin_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(22,'LinkedIn Accounts | Aged 1 Year | Connections','1 year aged LinkedIn accounts with 100+ connections. Established professional network included.',8.0,25,'/static/images/linkedin-account.png',8,'2025-07-22 07:54:27.361672','2025-07-22 07:54:27.361674','{"type": "linkedin_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(23,'TikTok Accounts | Fresh | Email Verified','Fresh TikTok accounts with email verification. Ready for content creation and viral marketing.',1.0,250,'/static/images/tiktok-account.png',15,'2025-07-22 07:54:27.367363','2025-07-22 07:54:27.367365','{"type": "tiktok_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(24,'TikTok Accounts | Phone Verified | USA','Phone verified TikTok accounts from USA. High quality for influencer marketing campaigns.',1.8000000000000000444,120,'/static/images/tiktok-account.png',15,'2025-07-22 07:54:27.371966','2025-07-22 07:54:27.371968','{"type": "tiktok_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(25,'TikTok Accounts | Aged 2 Months | Followers','2 months aged TikTok accounts with 500-1000 followers. Perfect for established content creators.',4.5,50,'/static/images/tiktok-account.png',15,'2025-07-22 07:54:27.376441','2025-07-22 07:54:27.376443','{"type": "tiktok_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(26,'Telegram Accounts | Phone Verified | Fresh','Fresh Telegram accounts with phone verification. Ready for messaging and channel management.',0.8000000000000000444,300,'/static/images/telegram-account.png',21,'2025-07-22 07:54:27.380760','2025-07-22 07:54:27.380762','{"type": "telegram_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(27,'Telegram Accounts | Premium Features | USA','Telegram accounts with premium features enabled. Perfect for business communication.',2.5,80,'/static/images/telegram-account.png',21,'2025-07-22 07:54:27.385614','2025-07-22 07:54:27.385615','{"type": "telegram_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(28,'Telegram Accounts | Aged 6 Months | Channels','6 months aged Telegram accounts with channel memberships. Established presence included.',3.5,45,'/static/images/telegram-account.png',21,'2025-07-22 07:54:27.390221','2025-07-22 07:54:27.390223','{"type": "telegram_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(29,'Snapchat Accounts | Email Verified | Fresh','Fresh Snapchat accounts with email verification. Ready for social media marketing and content sharing.',1.1999999999999999555,150,'/static/images/snapchat-account.png',18,'2025-07-22 07:54:27.394751','2025-07-22 07:54:27.394753','{"type": "snapchat_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(30,'Snapchat Accounts | Phone Verified | USA','Phone verified Snapchat accounts from USA. High quality for influencer marketing.',2.0,100,'/static/images/snapchat-account.png',18,'2025-07-22 07:54:27.399148','2025-07-22 07:54:27.399150','{"type": "snapchat_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(31,'Snapchat Accounts | Aged 3 Months | Friends','3 months aged Snapchat accounts with 50-100 friends. Perfect for established social presence.',3.7999999999999998223,60,'/static/images/snapchat-account.png',18,'2025-07-22 07:54:27.403669','2025-07-22 07:54:27.403670','{"type": "snapchat_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(32,'Reddit Accounts | Email Verified | Fresh','Fresh Reddit accounts with email verification. Ready for community engagement and marketing.',0.59999999999999997779,400,'/static/images/reddit-account.png',14,'2025-07-22 07:54:27.408259','2025-07-22 07:54:27.408261','{"type": "reddit_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(33,'Reddit Accounts | Aged 1 Month | Karma','1 month aged Reddit accounts with 100+ karma points. Perfect for community participation.',1.5,200,'/static/images/reddit-account.png',14,'2025-07-22 07:54:27.412674','2025-07-22 07:54:27.412676','{"type": "reddit_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
INSERT INTO product VALUES(34,'Reddit Accounts | High Karma | Aged 6 Months','6 months aged Reddit accounts with 1000+ karma. Established reputation for marketing.',5.0,50,'/static/images/reddit-account.png',14,'2025-07-22 07:54:27.417236','2025-07-22 07:54:27.417238','{"type": "reddit_account", "verification": "email_verified", "includes": ["credentials", "recovery_info"]}',0);
CREATE TABLE IF NOT EXISTS "order" (
	id INTEGER NOT NULL, 
	customer_name VARCHAR(100) NOT NULL, 
	customer_email VARCHAR(120) NOT NULL, 
	product_id INTEGER NOT NULL, 
	quantity INTEGER, 
	total_price FLOAT NOT NULL, 
	status VARCHAR(50), 
	payment_method VARCHAR(50), 
	account_details TEXT, 
	created_at DATETIME, 
	updated_at DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(product_id) REFERENCES product (id)
);
INSERT INTO "order" VALUES(1,'John Doe','john.doe@example.com',4,1,1.0200000000000000177,'completed','crypto','[{"username": "eewwevqq", "password": "VdncSzqJ7QSA", "email": "eewwevqq@yahoo.com", "additional_info": "Account ready for use"}]','2025-07-22 07:38:59.701291','2025-07-22 07:38:59.701293');
CREATE TABLE featured_products_section (
	id INTEGER NOT NULL, 
	homepage_section_id INTEGER NOT NULL, 
	product_ids TEXT, 
	max_products INTEGER, 
	sort_by VARCHAR(50), 
	sort_order VARCHAR(10), 
	created_at DATETIME, 
	updated_at DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(homepage_section_id) REFERENCES homepage_section (id)
);
COMMIT;
