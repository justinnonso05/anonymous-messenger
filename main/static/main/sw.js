const CACHE_NAME = 'anon-cache-v1';
const urlsToCache = Array.from(new Set([ // remove any duplicates
  '/',
  '/static/main/apple-touch-icon.png',
  '/static/main/favicon-96x96.png',
  '/static/main/favicon.ico',
  '/static/main/favicon.png',
  '/static/main/favicon.svg',
  '/static/main/logo.png',
  '/static/main/site.webmanifest',
  '/static/main/web-app-manifest-512x512.png',
  '/static/main/web-app-manifest-192x192.png',
]));

// Install event – caching assets
self.addEventListener('install', (event) => {
  console.log('[ServiceWorker] Installing');
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('[ServiceWorker] Caching app shell');
      return cache.addAll(urlsToCache);
    })
  );
  self.skipWaiting(); // Activate the new SW immediately
});

// Fetch event – serve from cache, fall back to network
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});

// Activate event – cleanup old caches
self.addEventListener('activate', (event) => {
  console.log('[ServiceWorker] Activated');
  event.waitUntil(
    caches.keys().then((keyList) => {
      return Promise.all(
        keyList.map((key) => {
          if (key !== CACHE_NAME) {
            console.log('[ServiceWorker] Removing old cache:', key);
            return caches.delete(key);
          }
        })
      );
    })
  );
  self.clients.claim(); // Take control of all clients right away
});
