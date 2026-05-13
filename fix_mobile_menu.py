import os
import re

# The perfect header and mobile menu drawer block
# Note: I'm putting the drawer INSIDE the header tag to ensure it's handled as one unit.
header_and_drawer_template = """    <!-- Header -->
    <header id="main-header" class="fixed w-full z-50 transition-all duration-300 bg-white shadow-md py-4">
        <div class="container mx-auto px-4">
            <div class="flex items-center justify-between h-20 transition-all duration-300" id="header-container">
                <a href="index.html" class="flex items-center gap-3">
                    <img src="assets/logos/logo.png" alt="RV Global Aviation Logo" class="h-16 w-auto transition-all duration-300" id="logo-img">
                </a>
                
                <!-- Desktop Navigation -->
                <nav class="hidden lg:flex items-center space-x-1">
                    <!-- Home -->
                    <div class="relative group">
                        <a href="index.html" class="font-medium text-[15px] transition-colors px-4 py-2 rounded-md flex items-center gap-1 {home_class}">Home</a>
                    </div>
                    
                    <!-- Services -->
                    <div class="relative group">
                        <a href="services.html" class="font-medium text-[15px] transition-colors px-4 py-2 rounded-md flex items-center gap-1 {services_class} group-hover:text-accent">
                            Services <svg class="w-4 h-4 transition-transform duration-300 group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                        </a>
                        <div class="absolute left-0 mt-0 w-64 bg-white rounded-xl shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 py-4 z-50 transform translate-y-2 group-hover:translate-y-0">
                            <a href="private-jet.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Private Jet Charter</a>
                            <a href="group-charter.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Group Charter</a>
                            <a href="cargo-charter.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Cargo Charter</a>
                            <a href="helicopter.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Helicopter Charter</a>
                        </div>
                    </div>
                    
                    <!-- Aircraft Guide -->
                    <div class="relative group">
                        <a href="aircraft.html" class="font-medium text-[15px] transition-colors px-4 py-2 rounded-md flex items-center gap-1 {aircraft_class} group-hover:text-accent">
                            Aircraft Guide <svg class="w-4 h-4 transition-transform duration-300 group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                        </a>
                        <div class="absolute left-0 mt-0 w-64 bg-white rounded-xl shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 py-4 z-50 max-h-[80vh] overflow-y-auto transform translate-y-2 group-hover:translate-y-0">
                            <a href="aircraft.html" class="block px-6 py-3 text-[14px] text-primary hover:text-accent hover:bg-gray-50 font-bold border-b border-gray-50 mb-2">Fleet Overview</a>
                            <a href="citation-m2.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Citation M2</a>
                            <a href="phenom-300e.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Phenom 300E</a>
                            <a href="challenger-350.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Challenger 350</a>
                            <a href="g650er.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Gulfstream G650ER</a>
                            <a href="global-7500.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Global 7500</a>
                            <a href="bell-407gxi.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Bell 407GXi</a>
                            <a href="pilatus-pc-12.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Pilatus PC-12 NGX</a>
                            <a href="legacy-600.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Legacy 600</a>
                            <a href="hawker-800xp.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Hawker 800XP</a>
                            <a href="citation-x.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Citation X+</a>
                            <a href="king-air-350i.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">King Air 350i</a>
                            <a href="h145.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Airbus H145</a>
                        </div>
                    </div>
                    
                    <!-- Destinations -->
                    <div class="relative group">
                        <a href="destinations.html" class="font-medium text-[15px] transition-colors px-4 py-2 rounded-md flex items-center gap-1 {destinations_class} group-hover:text-accent">
                            Destinations <svg class="w-4 h-4 transition-transform duration-300 group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                        </a>
                        <div class="absolute left-0 mt-0 w-64 bg-white rounded-xl shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 py-4 z-50 transform translate-y-2 group-hover:translate-y-0">
                            <a href="destinations.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Aspen</a>
                            <a href="destinations.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Maldives</a>
                            <a href="destinations.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">St. Barts</a>
                            <a href="destinations.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Mykonos</a>
                            <a href="destinations.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Dubai</a>
                            <a href="destinations.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">London</a>
                            <a href="destinations.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Paris</a>
                            <a href="destinations.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Geneva</a>
                        </div>
                    </div>
                    
                    <!-- About Us -->
                    <div class="relative group">
                        <a href="about.html" class="font-medium text-[15px] transition-colors px-4 py-2 rounded-md flex items-center gap-1 {about_class} group-hover:text-accent">
                            About Us <svg class="w-4 h-4 transition-transform duration-300 group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                        </a>
                        <div class="absolute left-0 mt-0 w-64 bg-white rounded-xl shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 py-4 z-50 transform translate-y-2 group-hover:translate-y-0">
                            <a href="about.html#story" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Our Story</a>
                            <a href="about.html#vision" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Our Vision</a>
                            <a href="about.html#team" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Our Team</a>
                        </div>
                    </div>
                    
                    <!-- Blog -->
                    <div class="relative group">
                        <a href="blog.html" class="font-medium text-[15px] transition-colors px-4 py-2 rounded-md flex items-center gap-1 {blog_class} group-hover:text-accent">
                            Blog <svg class="w-4 h-4 transition-transform duration-300 group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                        </a>
                        <div class="absolute left-0 mt-0 w-64 bg-white rounded-xl shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 py-4 z-50 transform translate-y-2 group-hover:translate-y-0">
                            <a href="blog.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Latest Articles</a>
                            <a href="blog.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Travel Tips</a>
                        </div>
                    </div>
                    
                    <a href="contact.html" class="font-medium text-[15px] transition-colors px-4 py-2 rounded-md {contact_class} hover:text-accent">Contact</a>
                </nav>

                <!-- CTA Button -->
                <div class="hidden lg:flex items-center space-x-4">
                    <a href="contact.html" class="bg-accent hover:bg-accent/90 text-white font-medium px-6 py-2 rounded-md transition-all shadow-sm hover:shadow-md">Inquire Now</a>
                </div>

                <!-- Mobile Menu Button -->
                <button id="mobile-menu-btn" class="lg:hidden p-2 text-primary hover:text-accent transition-colors">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
                </button>
            </div>
        </div>

        <!-- Mobile Menu Drawer (Floating Card Style) -->
        <div id="mobile-menu-drawer" class="fixed inset-0 z-[100] invisible transition-all duration-300">
            <!-- Backdrop -->
            <div id="mobile-menu-backdrop" class="absolute inset-0 bg-black/40 opacity-0 transition-opacity duration-300"></div>
            
            <!-- Drawer Content (Floating Card) -->
            <div id="mobile-menu-content" class="absolute right-4 top-4 bottom-4 w-[calc(100%-32px)] max-w-[350px] bg-white translate-x-full transition-transform duration-300 flex flex-col rounded-[2.5rem] shadow-2xl overflow-hidden">
                <!-- Drawer Header -->
                <div class="p-8 flex items-center justify-between">
                    <img src="assets/logos/logo.png" alt="Logo" class="h-10 w-auto">
                    <button id="mobile-menu-close" class="p-2 text-primary hover:text-accent transition-colors">
                        <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                    </button>
                </div>
                
                <!-- Navigation Links -->
                <div class="flex-1 overflow-y-auto px-8 py-4">
                    <nav class="flex flex-col space-y-6">
                        <a href="index.html" class="{home_mobile_class} font-bold text-xl">Home</a>
                        
                        <!-- Services Dropdown -->
                        <div>
                            <button class="w-full flex items-center justify-between {services_mobile_class} font-bold text-xl mobile-dropdown-btn" data-target="mobile-services">
                                Services <svg class="w-5 h-5 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </button>
                            <div id="mobile-services" class="hidden pl-4 mt-4 space-y-4 border-l-2 border-gray-100">
                                <a href="private-jet.html" class="block text-gray-500 hover:text-accent font-medium">Private Jet Charter</a>
                                <a href="group-charter.html" class="block text-gray-500 hover:text-accent font-medium">Group Charter</a>
                                <a href="cargo-charter.html" class="block text-gray-500 hover:text-accent font-medium">Cargo Charter</a>
                                <a href="helicopter.html" class="block text-gray-500 hover:text-accent font-medium">Helicopter Charter</a>
                            </div>
                        </div>

                        <!-- Aircraft Guide Dropdown -->
                        <div>
                            <button class="w-full flex items-center justify-between {aircraft_mobile_class} font-bold text-xl mobile-dropdown-btn" data-target="mobile-aircraft">
                                Aircraft Guide <svg class="w-5 h-5 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </button>
                            <div id="mobile-aircraft" class="hidden pl-4 mt-4 space-y-4 border-l-2 border-gray-100">
                                <a href="aircraft.html" class="block text-gray-500 hover:text-accent font-bold">Fleet Overview</a>
                                <a href="citation-m2.html" class="block text-gray-500 hover:text-accent">Citation M2</a>
                                <a href="phenom-300e.html" class="block text-gray-500 hover:text-accent">Phenom 300E</a>
                                <a href="challenger-350.html" class="block text-gray-500 hover:text-accent">Challenger 350</a>
                                <a href="g650er.html" class="block text-gray-500 hover:text-accent">Gulfstream G650ER</a>
                                <a href="global-7500.html" class="block text-gray-500 hover:text-accent">Global 7500</a>
                                <a href="bell-407gxi.html" class="block text-gray-500 hover:text-accent">Bell 407GXi</a>
                                <a href="pilatus-pc-12.html" class="block text-gray-500 hover:text-accent">Pilatus PC-12 NGX</a>
                                <a href="legacy-600.html" class="block text-gray-500 hover:text-accent">Legacy 600</a>
                                <a href="hawker-800xp.html" class="block text-gray-500 hover:text-accent">Hawker 800XP</a>
                                <a href="citation-x.html" class="block text-gray-500 hover:text-accent">Citation X+</a>
                                <a href="king-air-350i.html" class="block text-gray-500 hover:text-accent">King Air 350i</a>
                                <a href="h145.html" class="block text-gray-500 hover:text-accent">Airbus H145</a>
                            </div>
                        </div>

                        <!-- Destinations Dropdown -->
                        <div>
                            <button class="w-full flex items-center justify-between {destinations_mobile_class} font-bold text-xl mobile-dropdown-btn" data-target="mobile-destinations">
                                Destinations <svg class="w-5 h-5 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </button>
                            <div id="mobile-destinations" class="hidden pl-4 mt-4 space-y-4 border-l-2 border-gray-100">
                                <a href="destinations.html" class="block text-gray-500 hover:text-accent font-bold">All Destinations</a>
                                <a href="destinations.html" class="block text-gray-500 hover:text-accent">Aspen</a>
                                <a href="destinations.html" class="block text-gray-500 hover:text-accent">Maldives</a>
                                <a href="destinations.html" class="block text-gray-500 hover:text-accent">St. Barts</a>
                                <a href="destinations.html" class="block text-gray-500 hover:text-accent">Mykonos</a>
                                <a href="destinations.html" class="block text-gray-500 hover:text-accent">Dubai</a>
                                <a href="destinations.html" class="block text-gray-500 hover:text-accent">London</a>
                                <a href="destinations.html" class="block text-gray-500 hover:text-accent">Paris</a>
                                <a href="destinations.html" class="block text-gray-500 hover:text-accent">Geneva</a>
                            </div>
                        </div>

                        <!-- About Us Dropdown -->
                        <div>
                            <button class="w-full flex items-center justify-between {about_mobile_class} font-bold text-xl mobile-dropdown-btn" data-target="mobile-about">
                                About Us <svg class="w-5 h-5 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </button>
                            <div id="mobile-about" class="hidden pl-4 mt-4 space-y-4 border-l-2 border-gray-100">
                                <a href="about.html#story" class="block text-gray-500 hover:text-accent">Our Story</a>
                                <a href="about.html#vision" class="block text-gray-500 hover:text-accent">Our Vision</a>
                                <a href="about.html#team" class="block text-gray-500 hover:text-accent">Our Team</a>
                            </div>
                        </div>

                        <!-- Blog Dropdown -->
                        <div>
                            <button class="w-full flex items-center justify-between {blog_mobile_class} font-bold text-xl mobile-dropdown-btn" data-target="mobile-blog">
                                Blog <svg class="w-5 h-5 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </button>
                            <div id="mobile-blog" class="hidden pl-4 mt-4 space-y-4 border-l-2 border-gray-100">
                                <a href="blog.html" class="block text-gray-500 hover:text-accent">Latest News</a>
                                <a href="blog.html" class="block text-gray-500 hover:text-accent">Travel Guides</a>
                            </div>
                        </div>

                        <a href="contact.html" class="{contact_mobile_class} font-bold text-xl">Contact</a>
                    </nav>
                </div>
                
                <!-- Drawer Footer -->
                <div class="p-8 bg-gray-50/50 mt-auto">
                    <a href="tel:+918904886662" class="flex items-center gap-3 text-primary hover:text-accent mb-6 transition-colors">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
                        <span class="font-bold text-gray-600">+91 8904886662</span>
                    </a>
                    <a href="contact.html" class="block w-full bg-accent hover:bg-accent/90 text-white text-center py-4 rounded-2xl font-bold transition-all shadow-lg shadow-accent/20">Inquire Now</a>
                </div>
            </div>
        </div>
    </header>"""

directory = r"c:\Users\MSI\OneDrive\Desktop\rvglobal2\converted_site"

# Lists of pages for categories
services_pages = ['services.html', 'private-jet.html', 'group-charter.html', 'cargo-charter.html', 'helicopter.html']
aircraft_pages = ['aircraft.html', 'citation-m2.html', 'phenom-300e.html', 'challenger-350.html', 'g650er.html', 'global-7500.html', 'bell-407gxi.html', 'pilatus-pc-12.html', 'legacy-600.html', 'hawker-800xp.html', 'citation-x.html', 'king-air-350i.html', 'h145.html', 'aircraft-detail.html']
destinations_pages = ['destinations.html', 'destination-detail.html']
about_pages = ['about.html']
blog_pages = ['blog.html', 'blog-1.html', 'blog-2.html', 'blog-3.html', 'blog-4.html', 'blog-5.html', 'blog-6.html', 'blog-post.html']
contact_pages = ['contact.html']

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Determine active classes
        home_class = "text-accent" if filename == "index.html" else "text-primary"
        services_class = "text-accent" if filename in services_pages else "text-primary"
        aircraft_class = "text-accent" if filename in aircraft_pages else "text-primary"
        destinations_class = "text-accent" if filename in destinations_pages else "text-primary"
        about_class = "text-accent" if filename in about_pages else "text-primary"
        blog_class = "text-accent" if filename in blog_pages else "text-primary"
        contact_class = "text-accent" if filename in contact_pages else "text-primary"

        home_mobile_class = "text-accent" if filename == "index.html" else "text-primary"
        services_mobile_class = "text-accent" if filename in services_pages else "text-primary"
        aircraft_mobile_class = "text-accent" if filename in aircraft_pages else "text-primary"
        destinations_mobile_class = "text-accent" if filename in destinations_pages else "text-primary"
        about_mobile_class = "text-accent" if filename in about_pages else "text-primary"
        blog_mobile_class = "text-accent" if filename in blog_pages else "text-primary"
        contact_mobile_class = "text-accent" if filename in contact_pages else "text-primary"

        formatted_header = header_and_drawer_template.format(
            home_class=home_class,
            services_class=services_class,
            aircraft_class=aircraft_class,
            destinations_class=destinations_class,
            about_class=about_class,
            blog_class=blog_class,
            contact_class=contact_class,
            home_mobile_class=home_mobile_class,
            services_mobile_class=services_mobile_class,
            aircraft_mobile_class=aircraft_mobile_class,
            destinations_mobile_class=destinations_mobile_class,
            about_mobile_class=about_mobile_class,
            blog_mobile_class=blog_mobile_class,
            contact_mobile_class=contact_mobile_class
        )

        # 1. First, find where the header starts and replace it entirely along with anything that looks like a mobile menu
        # We'll use a very aggressive regex to find the header and any surrounding mobile menu trash
        
        # This regex matches from the start of a header or a header comment, until the closing header tag, 
        # plus any immediately following mobile menu divs.
        
        # However, to be safe, we'll just search for the <header> tag and replace it.
        # But we also need to handle the fact that some files might have multiple mobile-menu-drawer things now.
        
        # Let's just find the <header> block and replace it.
        # And separately remove any other occurrences of mobile-menu-drawer or mobile-menu.
        
        new_content = re.sub(r'<header.*?</header>', formatted_header, content, flags=re.DOTALL)
        
        # Remove leftover mobile menu blocks
        new_content = re.sub(r'<div id="mobile-menu-drawer".*?</div>\s*</div>\s*</div>', '', new_content, flags=re.DOTALL)
        new_content = re.sub(r'<div id="mobile-menu".*?</div>\s*</div>', '', new_content, flags=re.DOTALL)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {filename}")
