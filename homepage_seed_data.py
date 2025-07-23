#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from src.models.user import db
from src.models.homepage import HomepageSection, SiteSettings
from src.main import app

def seed_homepage_data():
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()
        
        # Clear existing data
        HomepageSection.query.delete()
        SiteSettings.query.delete()
        
        # Create default homepage sections
        sections = [
            {
                'section_type': 'hero',
                'title': 'Welcome to AccsMarket',
                'content': 'Your trusted marketplace for social media accounts',
                'order_index': 1,
                'is_active': True,
                'background_color': '#1f2937',
                'text_color': '#ffffff',
                'button_text': 'Browse Accounts',
                'button_url': '#products'
            },
            {
                'section_type': 'product_categories',
                'title': 'Available Account Categories',
                'content': 'Browse our wide selection of verified social media accounts',
                'order_index': 2,
                'is_active': True
            },
            {
                'section_type': 'info_block',
                'title': 'WHAT TO ASK BEFORE BUYING ACCOUNTS',
                'content': '''Regarding Social Media (SOMIA), it is evident that this is an effective and one of the most potent means capable of pitching in almost every business industry and market. Presently all the marketers use Social Media as a platform for steering customers. There are some difficulties you can meet when choosing the right Social Media sites for marketing purposes. It won't be confusing if you initially define the Social Media requirements that are to be used and choose the right supplier of Social Media accounts.

**- Where most of the target audiences are?**

It is essential to determine where the target audiences are spending their time. This could be Instagram or Facebook or Twitter, whatever, but the thing is that purchased accounts with followers are to be profitable in marketing.

**- Where is the activity of accounts reflected?**

The inactive accounts of Social Media are useless, even if they are accessible and well promoted. It is recommended to buy only active accounts.

**- What are the search results of followers?**

Try to determine what the users are searching for on SOMIA. This will bring you closer to profit.

**- What Social Media meets your niche better than others?**

It is worth considering that you may not get leads from Social Media used by other business owners. Therefore, choose the Social Media sites that correspond to your niche.''',
                'order_index': 3,
                'is_active': True,
                'background_color': '#ffffff',
                'text_color': '#374151'
            }
        ]
        
        for section_data in sections:
            section = HomepageSection(**section_data)
            db.session.add(section)
        
        # Create default site settings
        settings = [
            {
                'setting_key': 'site_title',
                'setting_value': 'AccsMarket - Buy Social Media Accounts',
                'setting_type': 'text',
                'description': 'Main site title displayed in browser tab'
            },
            {
                'setting_key': 'site_description',
                'setting_value': 'Your trusted marketplace for verified social media accounts',
                'setting_type': 'text',
                'description': 'Site description for SEO'
            },
            {
                'setting_key': 'header_logo_text',
                'setting_value': 'ACCS',
                'setting_type': 'text',
                'description': 'Logo text displayed in header'
            },
            {
                'setting_key': 'header_logo_subtext',
                'setting_value': 'market.com',
                'setting_type': 'text',
                'description': 'Logo subtext displayed in header'
            },
            {
                'setting_key': 'footer_copyright',
                'setting_value': '© 2024 AccsMarket. All rights reserved.',
                'setting_type': 'text',
                'description': 'Copyright text in footer'
            },
            {
                'setting_key': 'contact_email',
                'setting_value': 'support@accsmarket.com',
                'setting_type': 'text',
                'description': 'Contact email address'
            },
            {
                'setting_key': 'enable_search',
                'setting_value': 'true',
                'setting_type': 'boolean',
                'description': 'Enable/disable search functionality'
            },
            {
                'setting_key': 'products_per_page',
                'setting_value': '20',
                'setting_type': 'number',
                'description': 'Number of products to display per page'
            }
        ]
        
        for setting_data in settings:
            setting = SiteSettings(**setting_data)
            db.session.add(setting)
        
        db.session.commit()
        print("Homepage seed data created successfully!")

if __name__ == '__main__':
    seed_homepage_data()

