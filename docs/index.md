<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your App's Landing Page</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Font: Inter -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        .bg-pattern {
            background-image: linear-gradient(rgba(17, 24, 39, 0.8), rgba(17, 24, 39, 0.8)), url('https://placehold.co/1200x800/111827/1f2937?text=');
            background-size: cover;
            background-position: center;
        }
        /* Custom scrollbar styling */
        ::-webkit-scrollbar {
            width: 12px;
        }
        ::-webkit-scrollbar-track {
            background: #1f2937;
            border-radius: 10px;
        }
        ::-webkit-scrollbar-thumb {
            background: #4b5563;
            border-radius: 10px;
            border: 3px solid #1f2937;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #6b7280;
        }
    </style>
</head>
<body class="bg-gray-900 text-gray-300 overflow-x-hidden">

    <!-- Header & Navigation -->
    <header class="fixed top-0 left-0 w-full z-50 bg-gray-900 bg-opacity-70 backdrop-blur-md">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8 py-4 flex justify-between items-center">
            <a href="#" class="text-2xl font-bold text-white">YourApp</a>
            <nav class="hidden md:flex space-x-8">
                <a href="#features" class="text-white hover:text-indigo-400 transition-colors duration-300">Features</a>
                <a href="#about" class="text-white hover:text-indigo-400 transition-colors duration-300">About</a>
                <a href="#contact" class="text-white hover:text-indigo-400 transition-colors duration-300">Contact</a>
            </nav>
            <a href="#" class="hidden md:block bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-6 rounded-full shadow-lg transition-transform duration-300 transform hover:scale-105">Get Started</a>
            <!-- Mobile Menu Button -->
            <button id="mobile-menu-button" class="md:hidden text-white focus:outline-none">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path></svg>
            </button>
        </div>
        <!-- Mobile Menu -->
        <div id="mobile-menu" class="hidden md:hidden bg-gray-800 py-4 transition-all duration-300 ease-in-out">
            <nav class="flex flex-col items-center space-y-4">
                <a href="#features" class="block text-white hover:text-indigo-400 transition-colors duration-300">Features</a>
                <a href="#about" class="block text-white hover:text-indigo-400 transition-colors duration-300">About</a>
                <a href="#contact" class="block text-white hover:text-indigo-400 transition-colors duration-300">Contact</a>
                <a href="#" class="block bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-6 rounded-full transition-transform duration-300 transform hover:scale-105">Get Started</a>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="bg-pattern text-center py-20 md:py-32 lg:py-48 flex items-center justify-center min-h-screen">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8 max-w-4xl">
            <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-white leading-tight mb-4">
                The App That Makes Your Life Easier
            </h1>
            <p class="text-lg sm:text-xl lg:text-2xl text-gray-400 mb-8 max-w-2xl mx-auto">
                Discover a new way to manage your tasks, connect with people, and achieve your goals. Simple, powerful, and elegant.
            </p>
            <a href="#" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-3 px-8 rounded-full shadow-xl transition-all duration-300 transform hover:scale-105">
                Download Now
            </a>
        </div>
    </section>

    <!-- Features Section -->
    <section id="features" class="py-20 bg-gray-900">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-12">
                <h2 class="text-3xl sm:text-4xl font-bold text-white mb-4">Powerful Features</h2>
                <p class="text-gray-400 text-lg max-w-3xl mx-auto">
                    Our app is built with everything you need to succeed. Simple yet powerful tools right at your fingertips.
                </p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">

                <!-- Feature 1 -->
                <div class="bg-gray-800 p-8 rounded-xl shadow-lg transition-transform duration-300 hover:scale-105">
                    <div class="flex items-center justify-center w-16 h-16 bg-indigo-600 rounded-full mb-6">
                        <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-2">Blazing Fast Performance</h3>
                    <p class="text-gray-400">Experience a fluid and responsive interface with our optimized code and modern architecture.</p>
                </div>

                <!-- Feature 2 -->
                <div class="bg-gray-800 p-8 rounded-xl shadow-lg transition-transform duration-300 hover:scale-105">
                    <div class="flex items-center justify-center w-16 h-16 bg-indigo-600 rounded-full mb-6">
                        <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"></path></svg>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-2">Seamless Integration</h3>
                    <p class="text-gray-400">Connect with your favorite tools and services effortlessly. Our app plays well with others.</p>
                </div>

                <!-- Feature 3 -->
                <div class="bg-gray-800 p-8 rounded-xl shadow-lg transition-transform duration-300 hover:scale-105">
                    <div class="flex items-center justify-center w-16 h-16 bg-indigo-600 rounded-full mb-6">
                        <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.081 12.081 0 003 12c0 2.83 1.157 5.462 3.041 7.424a13.044 13.044 0 005.973 2.576 13.044 13.044 0 005.973-2.576c1.884-1.962 3.041-4.594 3.041-7.424 0-4.664-3.535-8.484-8-9.056z"></path></svg>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-2">Unbreakable Security</h3>
                    <p class="text-gray-400">Your data is our top priority. We use industry-leading encryption to keep your information safe.</p>
                </div>

            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="py-20 bg-gray-800">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
                <div>
                    <img src="https://placehold.co/600x400/1f2937/d1d5db?text=App+Screenshot" alt="App Screenshot" class="rounded-xl shadow-2xl transition-transform duration-300 transform hover:scale-105">
                </div>
                <div>
                    <h2 class="text-3xl sm:text-4xl font-bold text-white mb-4">About Our App</h2>
                    <p class="text-gray-400 text-lg mb-6">
                        Born from a need for simplicity and efficiency, our app was built to solve a problem we all face: information overload. We believe that technology should serve you, not the other way around. Our dedicated team of developers and designers has poured their passion into creating an experience that is both functional and beautiful.
                    </p>
                    <p class="text-gray-400 text-lg">
                        We are committed to continuous improvement, with regular updates and new features based on your feedback. Join our community and help us shape the future of productivity!
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Call to Action Section -->
    <section id="contact" class="py-20 bg-gray-900">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <div class="bg-gray-800 p-10 rounded-xl max-w-3xl mx-auto shadow-2xl">
                <h2 class="text-3xl sm:text-4xl font-bold text-white mb-4">Ready to Get Started?</h2>
                <p class="text-gray-400 text-lg mb-8">
                    Download the app today and start your journey towards a more organized and productive life.
                </p>
                <a href="#" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-3 px-10 rounded-full shadow-xl transition-all duration-300 transform hover:scale-105">
                    Join the Community
                </a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-900 py-8 border-t border-gray-700">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8 text-center text-gray-400">
            <p>&copy; <span id="current-year"></span> Your App Name. All rights reserved.</p>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // Set current year in the footer
            document.getElementById('current-year').textContent = new Date().getFullYear();

            // Mobile menu toggle
            const mobileMenuButton = document.getElementById('mobile-menu-button');
            const mobileMenu = document.getElementById('mobile-menu');

            mobileMenuButton.addEventListener('click', () => {
                mobileMenu.classList.toggle('hidden');
            });
            
            // Close mobile menu when a link is clicked
            const mobileLinks = mobileMenu.querySelectorAll('a');
            mobileLinks.forEach(link => {
                link.addEventListener('click', () => {
                    mobileMenu.classList.add('hidden');
                });
            });

            // Smooth scrolling for navigation links
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();
                    document.querySelector(this.getAttribute('href')).scrollIntoView({
                        behavior: 'smooth'
                    });
                });
            });
        });
    </script>
</body>
</html>
