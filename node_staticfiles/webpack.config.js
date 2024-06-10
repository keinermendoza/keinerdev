const path = require('path');

module.exports = {
    entry: {
        vendor: './src/vendor.js',
        expression_list: './src/expression_list.js',
        blog: './src/blog.js',

        // vendor: {
            // import: './src/vendor.js',
            // dependOn: 'shared',
        // },
        // expression_list: {
	    // import: './src/expression_list.js',
	    // dependOn: 'shared',
        // },
        // shared: 'swiper',
    },
    output: {
        'path': path.resolve(path.dirname(__dirname), 'project', 'staticfiles', 'js'),
        'filename': '[name].js'
    },
    // optimization: {
    //     runtimeChunk: 'single',
    // },
    module: {
        rules: [
            {
                test: /\.css$/i,
                use: [
                    'style-loader',
                    'css-loader'
                ]
            },
            {
                test: /\.(png|svg|jpg|jpeg|gif)$/i,
                type: 'asset/resource',
            },
        ]
    }
}
