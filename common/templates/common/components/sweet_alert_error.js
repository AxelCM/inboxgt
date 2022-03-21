{% if messages %}
    {% for message in messages %}
        {% if message.level == DEFAULT_MESSAGE_LEVELS.ERROR %}
        Swal.fire({
          icon: 'error',
          title: 'Error, algo salio mal!',
          text: '{{ message }}',
          })
        {% endif %}
    {% endfor %}
{% endif %}
