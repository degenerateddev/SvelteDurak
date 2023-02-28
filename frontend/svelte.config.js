import adapter from '@sveltejs/adapter-auto';
import { vitePreprocess } from '@sveltejs/kit/vite';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		adapter: adapter(),
		alias: {
			"admin-comps": "src/admin-components",
			"comps": "src/components"
		}
	},
	preprocess: [
		vitePreprocess({
			postcss: true
		})
	],
	vitePlugin: {
		experimental: {
			inspector: {
				holdMode: true,
			}
		}
	}

	/*kit: {
		adapter: adapter(),
		vite: {
			server: {
				proxy: {
					'/api' : {
						target: 'http://127.0.0.1:8000',
						rewrite: (path) => path.replace(/^\/api/, ''),
						changeOrigin: true,
					}
				}
			}
		}
	},*/
};

export default config;
