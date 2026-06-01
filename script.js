document.addEventListener('DOMContentLoaded', () => {
    // ==========================================
    // 1. HELPER FUNCTIONS
    // ==========================================
    const revealOnScroll = () => {
        const reveals = document.querySelectorAll('.reveal, .animate-on-scroll');
        reveals.forEach(el => {
            const windowHeight = window.innerHeight;
            const elementTop = el.getBoundingClientRect().top;
            const elementVisible = 150;
            if (elementTop < windowHeight - elementVisible) {
                el.classList.add('visible');
            }
        });
    };

    // ==========================================
    // 2. UI COMPONENTS (Navigation, Sliders, etc.)
    // ==========================================
    
    // Active Navigation Highlighting
    const highlightActiveLink = () => {
        const currentPath = window.location.pathname.split('/').pop() || 'index.html';
        const navLinks = document.querySelectorAll('nav a, #mobile-menu-content a');
        
        navLinks.forEach(link => {
            const linkPath = link.getAttribute('href');
            if (linkPath === currentPath) {
                link.classList.add('text-accent');
                link.classList.remove('text-primary', 'text-gray-500');
                
                // Desktop dropdown parent
                const parentDropdown = link.closest('.group');
                if (parentDropdown) {
                    const dropdownBtn = parentDropdown.querySelector('a');
                    if (dropdownBtn && dropdownBtn !== link) {
                        dropdownBtn.classList.add('text-accent');
                    }
                }

                // Mobile dropdown parent & auto-expand
                const mobileTarget = link.closest('div[id^="mobile-"]');
                if (mobileTarget) {
                    const mobileBtn = document.querySelector(`[data-target="${mobileTarget.id}"]`);
                    if (mobileBtn) {
                        mobileBtn.classList.add('text-accent');
                        mobileBtn.classList.remove('text-primary');
                        mobileTarget.classList.remove('hidden');
                        const icon = mobileBtn.querySelector('svg');
                        icon?.classList.add('rotate-180');
                    }
                }
            }
        });
    };
    highlightActiveLink();
    
    // Header Scroll Effect
    const header = document.getElementById('main-header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 20) header?.classList.add('scrolled');
        else header?.classList.remove('scrolled');
    });

    // Mobile Menu Toggle (Drawer Logic)
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenuDrawer = document.getElementById('mobile-menu-drawer');
    const mobileMenuBackdrop = document.getElementById('mobile-menu-backdrop');
    const mobileMenuContent = document.getElementById('mobile-menu-content');
    const mobileMenuClose = document.getElementById('mobile-menu-close');

                            const toggleMobileMenu = (open) => {
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
    };

    mobileMenuBtn?.addEventListener('click', () => toggleMobileMenu(true));
    mobileMenuClose?.addEventListener('click', () => toggleMobileMenu(false));
    mobileMenuBackdrop?.addEventListener('click', () => toggleMobileMenu(false));

    // Mobile Dropdowns
    const mobileDropdownBtns = document.querySelectorAll('.mobile-dropdown-btn');
    mobileDropdownBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetId = btn.getAttribute('data-target');
            const target = document.getElementById(targetId);
            const icon = btn.querySelector('svg');
            
            if (target) {
                const isHidden = target.classList.contains('hidden');
                target.classList.toggle('hidden');
                icon?.classList.toggle('rotate-180', isHidden);
            }
        });
    });

    // Hero Background Slider
    const slider = document.getElementById('hero-slider');
    if (slider) {
        const slides = slider.querySelectorAll('.slide');
        const dotsContainer = document.getElementById('slider-dots');
        let currentSlide = 0;
        let slideInterval;

        if (dotsContainer && dotsContainer.children.length === 0 && slides.length > 1) {
            slides.forEach((_, i) => {
                const dot = document.createElement('button');
                dot.className = `dot ${i === 0 ? 'bg-white w-8' : 'bg-white/50 w-2'} h-2 rounded-full transition-all`;
                dot.dataset.index = i;
                dotsContainer.appendChild(dot);
            });
        }

        const dots = slider.querySelectorAll('.dot');
        const prevBtn = document.getElementById('prev-slide');
        const nextBtn = document.getElementById('next-slide');

        const showSlide = (index) => {
            slides.forEach(s => { s.style.opacity = '0'; s.classList.replace('opacity-100', 'opacity-0'); });
            dots.forEach(d => { d.classList.remove('bg-white', 'w-8'); d.classList.add('bg-white/50', 'w-2'); });
            slides[index].style.opacity = '1';
            slides[index].classList.replace('opacity-0', 'opacity-100');
            if (dots[index]) { dots[index].classList.replace('bg-white/50', 'bg-white'); dots[index].classList.replace('w-2', 'w-8'); }
            currentSlide = index;
        };

        const startAutoPlay = () => { slideInterval = setInterval(() => showSlide((currentSlide + 1) % slides.length), 6000); };
        nextBtn?.addEventListener('click', () => { clearInterval(slideInterval); showSlide((currentSlide + 1) % slides.length); startAutoPlay(); });
        prevBtn?.addEventListener('click', () => { clearInterval(slideInterval); showSlide((currentSlide - 1 + slides.length) % slides.length); startAutoPlay(); });
        startAutoPlay();
    }

    // Hero Tabs logic (Passenger vs Cargo)
    const heroTabPassenger = document.getElementById('hero-tab-passenger');
    const heroTabCargo = document.getElementById('hero-tab-cargo');
    const noPassengersLabel = document.getElementById('no-passengers-label');

    heroTabPassenger?.addEventListener('click', (e) => {
        e.preventDefault();
        heroTabPassenger.classList.add('bg-accent'); heroTabPassenger.classList.remove('bg-primary');
        heroTabCargo?.classList.add('bg-primary'); heroTabCargo?.classList.remove('bg-accent');
        if (noPassengersLabel) noPassengersLabel.textContent = 'No. passengers';
    });

    heroTabCargo?.addEventListener('click', (e) => {
        e.preventDefault();
        heroTabCargo.classList.add('bg-accent'); heroTabCargo.classList.remove('bg-primary');
        heroTabPassenger?.classList.add('bg-primary'); heroTabPassenger?.classList.remove('bg-accent');
        if (noPassengersLabel) noPassengersLabel.textContent = 'Weight (kg)';
    });

    // ==========================================
    // INQUIRE NOW — Native Form Submission
    // ==========================================
    // The hero form now submits natively to Web3Forms without JS interception.

    // Content Tabs logic (Jets vs Destinations)
    const tabJets = document.getElementById('tab-jets');
    const tabDestinations = document.getElementById('tab-destinations');
    const jetsContent = document.getElementById('jets-content');
    const destinationsContent = document.getElementById('destinations-content');

    const updateTabs = (activeTab, inactiveTab, activeContent, inactiveContent) => {
        activeTab.classList.add('bg-accent', 'text-white'); activeTab.classList.remove('bg-gray-100', 'text-primary');
        activeTab.querySelector('.active-arrow')?.classList.remove('hidden');
        inactiveTab.classList.remove('bg-accent', 'text-white'); inactiveTab.classList.add('bg-gray-100', 'text-primary');
        inactiveTab.querySelector('.active-arrow')?.classList.add('hidden');
        activeContent.classList.remove('hidden'); inactiveContent.classList.add('hidden');
    };

    tabJets?.addEventListener('click', () => updateTabs(tabJets, tabDestinations, jetsContent, destinationsContent));
    tabDestinations?.addEventListener('click', () => updateTabs(tabDestinations, tabJets, destinationsContent, jetsContent));

    // Scroll Reveal Animation
    window.addEventListener('scroll', revealOnScroll);
    revealOnScroll(); // Initial check
});

// ==== Chatbot Loader ==== //
(function(){
  var link=document.createElement('link');
  link.rel='stylesheet';
  link.href='chatbot.css';
  document.head.appendChild(link);
  var script=document.createElement('script');
  script.src='chatbot.js';
  script.defer=true;
  document.body.appendChild(script);
})();
