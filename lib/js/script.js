$(function () {
  var includes = $("[data-include]");
  $.each(includes, function () {
    var file = "views/" + $(this).data("include") + ".html";
    $(this).load(file);
  });
});

const AlbumItem = ({ url, img, title }) => `
<div 
    class="col-xs-12 col-sm-4 col-md-4 col-lg-3 pull-left"
>
    <a 
    href="${url}" 
    class="thumbnail"
    >
    <img
        src="${img}"
        class="img-fluid"
        alt="${title}"

    />
    <div class="caption visible-lg">
        <h3>${title}</h3>
    </div>
    <div class="caption hidden-xs hidden-lg">
        <h4>${title}</h4>
    </div>
    <div class="caption visible-xs">
        <h5>${title}</h5>
    </div>
    </a>
</div>
`;

const ProductItem = ({ url, img, title }) => `
<div 
    class="col-xs-12 col-sm-4 col-md-4 col-lg-3 pull-left"
>
    <a 
    href="${url}" 
    class="thumbnail"
    >
    <img
        src="${img}"
        class="img-fluid"
        alt="${title}"

    />
    <div class="caption visible-lg">
        <h3>${title}</h3>
    </div>
    <div class="caption hidden-xs hidden-lg">
        <h4>${title}</h4>
    </div>
    <div class="caption visible-xs">
        <h5>${title}</h5>
    </div>
    </a>
</div>
`;

const SliderItem = ({ img, title }) => `
<li>
    <img
        src="${img}"
        class="img-responsive"
        alt="Image of ${title}"
        title="${title}"
    />
    </li>
`;

const QuoteItem = ({text, status}) => `
<div class="item ${status}">
    <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
        <h3>
        <em>
            <p class="text-center text-muted">
            " ${text} "
            </p>
        </em>
        </h3>
    </div>
</div>
`;