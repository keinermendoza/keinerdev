import './css/multi-select-tag.css';
import './css/markdownEditor.css';
import './js/markdownEditor';
import MultiSelectTag from  './js/multi-select-tag';


document.addEventListener("DOMContentLoaded", () => {
    // new MultiSelectTag('id_sources', {
    //     rounded: true,    // default true
    //     shadow: true,      // default false
    //     placeholder: 'Search',  // default Search...
    //     tagColor: {
    //         textColor: '#327b2c',
    //         borderColor: '#92e681',
    //         bgColor: '#eaffe6',
    //     },
    //     onChange: function(values) {
    //         console.log(values)
    //     }
    // });
    const helper_text = document.getElementById('filter_source_help_text').innerHTML;
    new MultiSelectTag('sources_filter_id', {
        rounded: true,    // default true
        shadow: true,      // default false
        placeholder: 'Search',  // default Search...
        helperText: helper_text,
        tagColor: {
            textColor: '#327b2c',
            borderColor: '#92e681',
            bgColor: '#eaffe6',
        },
        onChange: function(values) {
            const execFilter = new Event("excecute_expression_filtering");
            document.body.dispatchEvent(execFilter);
        }
    });
    
})