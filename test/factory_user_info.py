def create_user_info(name, email, password):
    return {
        "X-User-ID": name,
        "X-User-Email": email,
        "X-User-Role": 'user',
        "X-Permissions": '',
        'X-Token-Expires': 34324982
    }