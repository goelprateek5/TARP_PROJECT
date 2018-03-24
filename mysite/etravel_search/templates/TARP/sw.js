importScripts('/node_modules/workbox-sw/build/importScripts/workbox-sw.prod.v2.1.2.js');
const staticAssests =[
    './',
    './styles.css',
    './app.js',
    './node_modules/workbox-sw/build/importScripts/workbox-sw.prod.v2.1.2.js',
    './fallback.html',
    './bg-min.jpg',
    './manifest.json'
    
];

const wb= new WorkboxSW();
wb.precache(staticAssests);