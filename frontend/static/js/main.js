$(document).ready(function () {
  $.get('http://localhost:5000/risk_types').done(function (response) {
    for (var i = 0; i < response.length; i++) {
      processRiskType(response[i], i);
    }
  });

  function processRiskType(info, index) {
    var name = info['name'];
    var fields = info['fields'];
    $('#list').append("<div class='risk-type-name' data-idx='" + index + "'>Name: " + name + "</div>");
    for (var i = 0; i < fields.length; i++) {
      processFields(fields[i], index);
    }
  };

  function processFields(field, parent_index) {
    var parent = $('div[data-idx="'+ parent_index + '"]')[0];
    var info = field['info'];
    var name = field['name'];

    if (info['type'] != 'enum') {
      $(parent).append('<div class="field-name">' + name +
        ': <input class="field-value-' + info['type'] +'" type="' + info['type'] + '" value="' + info['value'] + '"/></div>');
      return;
    }

    if (info['type'] == 'enum') {
      $(parent).append('<span class="field-name">' + name + '</span>');
      var htmlString = '<select>';
      var options = info['options'];
      var selectedIndex = info['selected_index'];

      for (var i = 0; i < info['n_options']; i++) {
        htmlString += '<option value="' + options[i]['value'] + '"';

        if (i == selectedIndex) {
          htmlString += ' selected ';
        }
        htmlString += '>' + options[i]['value'] + '</option>';
      }

      htmlString += '</select>';
      $(parent).append(htmlString);
    }
  }
});