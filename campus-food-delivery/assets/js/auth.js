// assets/js/auth.js

document.addEventListener('DOMContentLoaded', () => {
    // Tab Switching
    const loginTab = document.getElementById('login-tab');
    const signupTab = document.getElementById('signup-tab');
    const loginForm = document.getElementById('login-form');
    const signupForm = document.getElementById('signup-form');

    if (loginTab && signupTab) {
        loginTab.addEventListener('click', () => {
            loginTab.classList.add('border-blue-500', 'text-blue-500');
            loginTab.classList.remove('border-gray-300', 'text-gray-500');
            signupTab.classList.remove('border-blue-500', 'text-blue-500');
            signupTab.classList.add('border-gray-300', 'text-gray-500');
            loginForm.classList.remove('hidden');
            signupForm.classList.add('hidden');
        });

        signupTab.addEventListener('click', () => {
            signupTab.classList.add('border-blue-500', 'text-blue-500');
            signupTab.classList.remove('border-gray-300', 'text-gray-500');
            loginTab.classList.remove('border-blue-500', 'text-blue-500');
            loginTab.classList.add('border-gray-300', 'text-gray-500');
            signupForm.classList.remove('hidden');
            loginForm.classList.add('hidden');
        });
    }

    // Handle Login Form Submission
    if (loginForm) {
        loginForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const phone = document.getElementById('login-phone').value;
            const pin = document.getElementById('login-pin').value;

            // TODO: Connect to backend API for authentication
            console.log('Login:', { phone, pin });

            fetch('http://127.0.0.1:5000/api/auth/login', { // Replace with actual API endpoint
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ phone, pin })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Redirect to stores page
                    window.location.href = 'stores.html';
                } else {
                    alert('Invalid phone number or PIN.');
                }
            })
            .catch(error => console.error('Error during login:', error));
        });
    }

    // Handle Signup Form Submission
    if (signupForm) {
        signupForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const phone = document.getElementById('signup-phone').value;
            const email = document.getElementById('signup-email').value;
            const otp = document.getElementById('signup-otp').value;

            // TODO: Connect to backend API for signup
            console.log('Signup:', { phone, email, otp });

            fetch('http://127.0.0.1:5000/api/auth/signup', { // Replace with actual API endpoint
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ phone, email, otp })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Redirect to stores page
                    window.location.href = 'stores.html';
                } else {
                    alert('Signup failed. Please try again.');
                }
            })
            .catch(error => console.error('Error during signup:', error));
        });

        // Handle Send OTP
        const sendOtpBtn = document.getElementById('send-otp');
        if (sendOtpBtn) {
            sendOtpBtn.addEventListener('click', () => {
                const email = document.getElementById('signup-email').value;

                // TODO: Connect to backend API to send OTP
                console.log('Send OTP to:', email);

                fetch('http://127.0.0.1:5000/api/auth/send-otp', { // Replace with actual API endpoint
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ email })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        alert('OTP sent to your email.');
                    } else {
                        alert('Failed to send OTP. Please try again.');
                    }
                })
                .catch(error => console.error('Error sending OTP:', error));
            });
        }
    }
});
