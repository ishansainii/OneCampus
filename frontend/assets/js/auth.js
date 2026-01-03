// assets/js/auth.js

document.addEventListener('DOMContentLoaded', () => {
    const loginTab = document.getElementById('login-tab');
    const signupTab = document.getElementById('signup-tab');
    const loginForm = document.getElementById('login-form');
    const signupForm = document.getElementById('signup-form');

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

    // Handle Login Form Submission
    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const phone = document.getElementById('login-phone').value;
        const pin = document.getElementById('login-pin').value;

        // TODO: Connect to backend API for authentication
        console.log('Login:', { phone, pin });

        // Example: Redirect to stores page on successful login
        // window.location.href = 'stores.html';
    });

    // Handle Signup Form Submission
    signupForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const phone = document.getElementById('signup-phone').value;
        const email = document.getElementById('signup-email').value;
        const otp = document.getElementById('signup-otp').value;

        // TODO: Connect to backend API for signup
        console.log('Signup:', { phone, email, otp });

        // Example: Redirect to stores page on successful signup
        // window.location.href = 'stores.html';
    });

    // Handle Send OTP
    document.getElementById('send-otp').addEventListener('click', () => {
        const email = document.getElementById('signup-email').value;

        // TODO: Connect to backend API to send OTP
        console.log('Send OTP to:', email);

        alert('OTP sent to your email.');
    });
});
