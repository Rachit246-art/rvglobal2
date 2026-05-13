/* chatbot.js - Fixed & Improved Vanilla Implementation */
(function() {
    // ----- Configuration & Content -----
    const steps = [
        { id: 0, type: 'choice', question: 'Welcome to RV Global Aviation. We specialize in premium private jet, helicopter, and international charter services. How may we assist you today?', options: ['Domestic Charter', 'International Charter', 'Helicopter Charter', 'Corporate Travel', 'Pilgrimage Charter', 'Emergency Charter', 'Speak to Aviation Expert'] },
        { id: 1, type: 'choice', question: 'Please select your travel requirement.', options: ['One Way', 'Round Trip', 'Multi-City', 'Same Day Return', 'Urgent Departure'] },
        { id: 2, type: 'text', question: 'Please enter your departure city or airport.', placeholder: 'e.g. New York' },
        { id: 3, type: 'text', question: 'Please enter your destination city or airport.', placeholder: 'e.g. London' },
        { id: 4, type: 'date', question: 'When would you like to fly?', placeholder: 'Select date' },
        { id: 5, type: 'choice', question: 'Please select your preferred departure timing.', options: ['Early Morning', 'Morning', 'Afternoon', 'Evening', 'Flexible Timing'] },
        { id: 6, type: 'choice', question: 'How many passengers will be traveling?', options: ['1-3 Passengers', '4-6 Passengers', '7-10 Passengers', '10+ Passengers'] },
        { id: 7, type: 'choice', question: 'Please select the purpose of your charter.', options: ['Business Travel', 'Leisure / Family', 'Religious Trip', 'Wedding / Event', 'Medical Emergency', 'VIP Movement', 'Corporate Team Travel'] },
        { id: 8, type: 'choice', question: 'Do you have a preferred aircraft category?', options: ['Light Jet', 'Mid-Size Jet', 'Heavy Jet', 'Turbo Prop', 'Helicopter', 'Suggest Best Option'] },
        { id: 9, type: 'choice', question: 'Would you require any additional premium services?', options: ['Luxury Ground Transfer', 'In-Flight Catering', 'Hotel Assistance', 'Visa Assistance', 'Concierge Services', 'Fast Track Airport Assistance', 'No Additional Services'] },
        { id: 10, type: 'choice', question: 'Please select your preferred charter experience.', options: ['Most Efficient Option', 'Premium Comfort', 'Ultra Luxury Experience'] },
        { id: 11, type: 'form', question: 'Please share your details so our aviation specialist can prepare aircraft availability and charter quotations.' }
    ];

    let currentStepIndex = 0;
    let userData = {};
    let isInitialized = false;

    // ----- UI Construction -----
    function initChatbot() {
        if (document.getElementById('chatbot-toggle')) return;

        // Toggle Button
        const toggleBtn = document.createElement('button');
        toggleBtn.id = 'chatbot-toggle';
        toggleBtn.innerHTML = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 01-2 2H5l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg>`;
        document.body.appendChild(toggleBtn);

        // Panel
        const panel = document.createElement('div');
        panel.id = 'chatbot-panel';
        panel.innerHTML = `
            <div class="chatbot-header">
                <div class="chatbot-header-info">
                    <img src="assets/logos/logo.png" alt="RV" onerror="this.src='https://via.placeholder.com/32'">
                    <div class="chatbot-header-text">
                        <h4>RV Global Aviation</h4>
                        <span>Online | Aviation Expert</span>
                    </div>
                </div>
                <button class="chatbot-close">✕</button>
            </div>
            <div class="chatbot-messages" id="chatbot-messages-list"></div>
            <div class="chatbot-footer" id="chatbot-input-area"></div>
        `;
        document.body.appendChild(panel);

        const msgList = document.getElementById('chatbot-messages-list');
        const inputArea = document.getElementById('chatbot-input-area');
        const closeBtn = panel.querySelector('.chatbot-close');

        // Toggle logic
        const toggleChat = () => {
            const isOpen = panel.classList.toggle('open');
            toggleBtn.classList.toggle('open');
            
            if (isOpen && !isInitialized) {
                renderStep(0);
                isInitialized = true;
            }
        };

        toggleBtn.addEventListener('click', toggleChat);
        closeBtn.addEventListener('click', toggleChat);

        // Rendering Steps
        function addMessage(type, content) {
            const time = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
            const msgDiv = document.createElement('div');
            msgDiv.className = `message ${type}`;
            msgDiv.innerHTML = `
                <div class="text">${content}</div>
                <div class="time">${time}</div>
            `;
            msgList.appendChild(msgDiv);
            msgList.scrollTop = msgList.scrollHeight;
        }

        function renderStep(index) {
            if (index >= steps.length) {
                inputArea.innerHTML = '';
                addMessage('bot', '<strong>Thank you for choosing RV Global Aviation.</strong><br>Your charter request has been submitted. Our aviation specialist will contact you shortly.');
                return;
            }

            const step = steps[index];
            currentStepIndex = index;
            
            // Add bot question
            setTimeout(() => {
                addMessage('bot', step.question);
                renderInput(step);
            }, 400);
        }

        function renderInput(step) {
            inputArea.innerHTML = '';

            if (step.type === 'choice') {
                const container = document.createElement('div');
                container.className = 'choice-container';
                step.options.forEach(opt => {
                    const btn = document.createElement('button');
                    btn.className = 'choice-btn';
                    btn.textContent = opt;
                    btn.onclick = () => handleUserInput(opt);
                    container.appendChild(btn);
                });
                inputArea.appendChild(container);
            } else if (step.type === 'text' || step.type === 'date') {
                const form = document.createElement('form');
                form.className = 'input-form';
                form.innerHTML = `
                    <input type="${step.type}" class="chat-input" placeholder="${step.placeholder || ''}" required>
                    <button type="submit" class="send-btn">Send</button>
                `;
                form.onsubmit = (e) => {
                    e.preventDefault();
                    const val = form.querySelector('input').value;
                    handleUserInput(val);
                };
                inputArea.appendChild(form);
                form.querySelector('input').focus();
            } else if (step.type === 'form') {
                const form = document.createElement('form');
                form.className = 'lead-form';
                form.innerHTML = `
                    <input type="text" name="name" placeholder="Full Name" required>
                    <input type="tel" name="phone" placeholder="Mobile Number" required>
                    <input type="email" name="email" placeholder="Email Address" required>
                    <input type="text" name="company" placeholder="Company (Optional)">
                    <button type="submit" class="submit-btn">Get Charter Quote</button>
                `;
                form.onsubmit = (e) => {
                    e.preventDefault();
                    const formData = new FormData(form);
                    userData.name = formData.get('name');
                    userData.phone = formData.get('phone');
                    userData.email = formData.get('email');
                    userData.company = formData.get('company');
                    handleUserInput(`Submitted details for ${userData.name}`);
                };
                inputArea.appendChild(form);
            }
        }

        function handleUserInput(value) {
            addMessage('user', value);
            
            if (value === 'Speak to Aviation Expert') {
                window.open('https://wa.me/918904886662', '_blank');
                return;
            }

            // Record data (index-based mapping)
            const keys = ['charterType', 'tripType', 'departure', 'destination', 'date', 'time', 'passengers', 'purpose', 'aircraft', 'additionalServices', 'experience'];
            if (currentStepIndex < keys.length) {
                userData[keys[currentStepIndex]] = value;
            }

            renderStep(currentStepIndex + 1);
        }
    }

    // Initialize on load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initChatbot);
    } else {
        initChatbot();
    }
})();
