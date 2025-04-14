const CACHE_NAME = 'anon-cache-v1';
const urlsToCache = [
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
  // Add more static assets if needed
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('[ServiceWorker] Caching files');
      return cache.addAll(urlsToCache);
    })
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});

self.addEventListener('activate', (event) => {
  console.log('[ServiceWorker] Activated');
});
