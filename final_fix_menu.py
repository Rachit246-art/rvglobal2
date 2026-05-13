import os
import re

# The perfect header and mobile menu drawer block
header_and_drawer_template = r"""    <!-- Header -->
    <header id="main-header" class="sticky top-0 w-full z-50 transition-all duration-300 bg-white shadow-md py-0">
        <div class="container mx-auto px-4">
            <div class="flex items-center justify-between h-24 transition-all duration-300" id="header-container">
                <a href="index.html" class="flex items-center gap-3">
                    <img src="assets/logos/logo.png" alt="RV Global Aviation Logo" class="h-20 w-auto transition-all duration-300" id="logo-img">
                </a>
                
                <!-- Desktop Navigation -->
                <nav class="hidden lg:flex items-center space-x-1">
                    <!-- Home -->
                    <div class="relative group">
                        <a href="index.html" class="font-medium text-[14px] transition-colors px-4 py-2 rounded-md flex items-center gap-1 {home_class}">Home</a>
                    </div>
                    
                    <!-- Services -->
                    <div class="relative group">
                        <a href="services.html" class="font-medium text-[14px] transition-colors px-4 py-2 rounded-md flex items-center gap-1 {services_class} group-hover:text-accent">
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
                        <a href="aircraft.html" class="font-medium text-[14px] transition-colors px-4 py-2 rounded-md flex items-center gap-1 {aircraft_class} group-hover:text-accent">
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
                        <a href="destinations.html" class="font-medium text-[14px] transition-colors px-4 py-2 rounded-md flex items-center gap-1 {destinations_class} group-hover:text-accent">
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
                        <a href="about.html" class="font-medium text-[14px] transition-colors px-4 py-2 rounded-md flex items-center gap-1 {about_class} group-hover:text-accent">
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
                        <a href="blog.html" class="font-medium text-[14px] transition-colors px-4 py-2 rounded-md flex items-center gap-1 {blog_class} group-hover:text-accent">
                            Blog <svg class="w-4 h-4 transition-transform duration-300 group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                        </a>
                        <div class="absolute left-0 mt-0 w-64 bg-white rounded-xl shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 py-4 z-50 transform translate-y-2 group-hover:translate-y-0">
                            <a href="blog.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Latest Articles</a>
                            <a href="blog.html" class="block px-6 py-2.5 text-[14px] text-primary hover:text-accent hover:bg-gray-50 transition-colors">Travel Tips</a>
                        </div>
                    </div>
                    
                    <a href="contact.html" class="font-medium text-[14px] transition-colors px-4 py-2 rounded-md {contact_class} hover:text-accent">Contact</a>
                </nav>

                <!-- CTA Button -->
                <div class="hidden lg:flex items-center space-x-4">
                    <a href="contact.html" class="bg-accent hover:bg-accent/90 text-white font-medium px-6 py-2 rounded-md transition-all shadow-sm hover:shadow-md text-sm">Inquire Now</a>
                </div>

                <!-- Mobile Menu Button -->
                <button id="mobile-menu-btn" class="lg:hidden p-2 text-primary hover:text-accent transition-colors">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
                </button>
            </div>
        </div>

        <!-- Mobile Menu Drawer (Premium Centered Card Style) -->
        <div id="mobile-menu-drawer" class="fixed inset-0 z-[100] invisible transition-all duration-500 flex items-center justify-center p-6">
            <!-- Backdrop -->
            <div id="mobile-menu-backdrop" class="absolute inset-0 bg-black/70 opacity-0 transition-opacity duration-500 backdrop-blur-md"></div>
            
            <!-- Drawer Content (Centered Card) -->
            <div id="mobile-menu-content" class="relative w-full max-w-[360px] max-h-[85vh] bg-white opacity-0 scale-95 transition-all duration-500 flex flex-col rounded-[3rem] shadow-[0_20px_50px_rgba(0,0,0,0.3)] overflow-hidden">
                <!-- Drawer Header -->
                <div class="pt-10 px-10 pb-6 flex items-center justify-between border-b border-gray-50">
                    <img src="assets/logos/logo.png" alt="Logo" class="h-9 w-auto">
                    <button id="mobile-menu-close" class="p-2 text-gray-400 hover:text-accent transition-colors">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                    </button>
                </div>
                
                <!-- Navigation Links -->
                <div class="flex-1 overflow-y-auto px-10 py-8">
                    <nav class="flex flex-col space-y-7">
                        <a href="index.html" class="{home_mobile_class} font-bold text-xl transition-colors">Home</a>
                        
                        <!-- Services Dropdown -->
                        <div>
                            <button class="w-full flex items-center justify-between {services_mobile_class} font-bold text-xl mobile-dropdown-btn transition-colors text-[#1a1a1a]" data-target="mobile-services">
                                Services <svg class="w-4 h-4 text-gray-400 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </button>
                            <div id="mobile-services" class="hidden pl-4 mt-6 space-y-5 border-l border-gray-100">
                                <a href="private-jet.html" class="block text-gray-500 hover:text-accent font-medium text-lg">Private Jet Charter</a>
                                <a href="group-charter.html" class="block text-gray-500 hover:text-accent font-medium text-lg">Group Charter</a>
                                <a href="cargo-charter.html" class="block text-gray-500 hover:text-accent font-medium text-lg">Cargo Charter</a>
                                <a href="helicopter.html" class="block text-gray-500 hover:text-accent font-medium text-lg">Helicopter Charter</a>
                            </div>
                        </div>

                        <!-- Aircraft Guide Dropdown -->
                        <div>
                            <button class="w-full flex items-center justify-between {aircraft_mobile_class} font-bold text-xl mobile-dropdown-btn transition-colors text-[#1a1a1a]" data-target="mobile-aircraft">
                                Aircraft Guide <svg class="w-4 h-4 text-gray-400 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </button>
                            <div id="mobile-aircraft" class="hidden pl-4 mt-6 space-y-5 border-l border-gray-100">
                                <a href="aircraft.html" class="block text-gray-500 hover:text-accent font-medium text-lg">Fleet Overview</a>
                                <a href="citation-m2.html" class="block text-gray-500 hover:text-accent font-medium text-lg">Citation M2</a>
                                <a href="phenom-300e.html" class="block text-gray-500 hover:text-accent font-medium text-lg">Phenom 300E</a>
                                <a href="challenger-350.html" class="block text-gray-500 hover:text-accent font-medium text-lg">Challenger 350</a>
                                <a href="g650er.html" class="block text-gray-500 hover:text-accent font-medium text-lg">Gulfstream G650ER</a>
                                <a href="global-7500.html" class="block text-gray-500 hover:text-accent font-medium text-lg">Global 7500</a>
                            </div>
                        </div>

                        <!-- Destinations Dropdown -->
                        <div>
                            <button class="w-full flex items-center justify-between {destinations_mobile_class} font-bold text-xl mobile-dropdown-btn transition-colors text-[#1a1a1a]" data-target="mobile-destinations">
                                Destinations <svg class="w-4 h-4 text-gray-400 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </button>
                            <div id="mobile-destinations" class="hidden pl-4 mt-6 space-y-5 border-l border-gray-100">
                                <a href="destinations.html" class="block text-gray-500 hover:text-accent font-medium text-lg">All Destinations</a>
                                <a href="destinations.html" class="block text-gray-500 hover:text-accent font-medium text-lg">Aspen</a>
                                <a href="destinations.html" class="block text-gray-500 hover:text-accent font-medium text-lg">Maldives</a>
                                <a href="destinations.html" class="block text-gray-500 hover:text-accent font-medium text-lg">St. Barts</a>
                            </div>
                        </div>

                        <!-- About Us Dropdown -->
                        <div>
                            <button class="w-full flex items-center justify-between {about_mobile_class} font-bold text-xl mobile-dropdown-btn transition-colors text-[#1a1a1a]" data-target="mobile-about">
                                About Us <svg class="w-4 h-4 text-gray-400 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </button>
                            <div id="mobile-about" class="hidden pl-4 mt-6 space-y-5 border-l border-gray-100">
                                <a href="about.html#story" class="block text-gray-500 hover:text-accent font-medium text-lg">Our Story</a>
                                <a href="about.html#vision" class="block text-gray-500 hover:text-accent font-medium text-lg">Our Vision</a>
                                <a href="about.html#team" class="block text-gray-500 hover:text-accent font-medium text-lg">Our Team</a>
                            </div>
                        </div>

                        <!-- Blog Dropdown -->
                        <div>
                            <button class="w-full flex items-center justify-between {blog_mobile_class} font-bold text-xl mobile-dropdown-btn transition-colors text-[#1a1a1a]" data-target="mobile-blog">
                                Blog <svg class="w-4 h-4 text-gray-400 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </button>
                            <div id="mobile-blog" class="hidden pl-4 mt-6 space-y-5 border-l border-gray-100">
                                <a href="blog.html" class="block text-gray-500 hover:text-accent font-medium text-lg">Latest News</a>
                                <a href="blog.html" class="block text-gray-500 hover:text-accent font-medium text-lg">Travel Guides</a>
                            </div>
                        </div>

                        <a href="contact.html" class="{contact_mobile_class} font-bold text-xl transition-colors text-[#1a1a1a]">Contact</a>
                    </nav>
                </div>
                
                <!-- Drawer Footer -->
                <div class="px-10 pb-10 pt-6 mt-auto bg-white border-t border-gray-50">
                    <a href="tel:+918904886662" class="flex items-center gap-4 text-primary hover:text-accent mb-6 transition-colors group">
                        <div class="w-9 h-9 rounded-full bg-[#E5F4FD] flex items-center justify-center text-accent transition-all group-hover:bg-accent group-hover:text-white">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
                        </div>
                        <span class="font-bold text-lg text-gray-700">+91 8904886662</span>
                    </a>
                    <a href="contact.html" class="block w-full bg-accent hover:bg-accent/90 text-white text-center py-4 rounded-xl font-bold text-xl transition-all shadow-lg shadow-accent/20 active:scale-[0.98]">Inquire Now</a>
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

        # 1. REMOVE ALL TRACES of mobile menus first
        content = re.sub(r'<!-- Mobile Menu Drawer.*?-->\s*<div id="mobile-menu-drawer".*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
        content = re.sub(r'<div id="mobile-menu-drawer".*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
        content = re.sub(r'<div id="mobile-menu".*?</div>\s*</div>', '', content, flags=re.DOTALL)
        
        # 2. REPLACE the header
        new_content = re.sub(r'<header.*?</header>', formatted_header, content, flags=re.DOTALL)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Final Fix Applied to {filename}")

# NOW UPDATE SCRIPT.JS FOR THE NEW ANIMATION
script_path = os.path.join(directory, 'script.js')
if os.path.exists(script_path):
    with open(script_path, 'r', encoding='utf-8') as f:
        js_content = f.read()

    # Replace the toggleMobileMenu function
    new_js_logic = r"""    const toggleMobileMenu = (open) => {
        if (!mobileMenuDrawer) return;
        
        if (open) {
            mobileMenuDrawer.classList.remove('invisible');
            mobileMenuDrawer.classList.add('visible');
            setTimeout(() => {
                mobileMenuBackdrop?.classList.add('opacity-100');
                mobileMenuContent?.classList.add('opacity-100', 'scale-100', 'translate-y-0');
                mobileMenuContent?.classList.remove('opacity-0', 'scale-95', 'translate-y-10');
            }, 10);
            document.body.style.overflow = 'hidden';
        } else {
            mobileMenuBackdrop?.classList.remove('opacity-100');
            mobileMenuContent?.classList.remove('opacity-100', 'scale-100', 'translate-y-0');
            mobileMenuContent?.classList.add('opacity-0', 'scale-95', 'translate-y-10');
            setTimeout(() => {
                mobileMenuDrawer?.classList.remove('visible');
                mobileMenuDrawer?.classList.add('invisible');
            }, 500);
            document.body.style.overflow = '';
        }
    };"""

    js_content = re.sub(r'const toggleMobileMenu = \(open\) => \{.*?\s*?\};', new_js_logic, js_content, flags=re.DOTALL)
    
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print("Updated script.js with new animation logic")
