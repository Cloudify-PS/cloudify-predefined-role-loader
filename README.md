# Predefined Role Loader

An implementation of [AbstractRoleLoader](https://github.com/cloudify-cosmo/flask-securest/blob/0.8/flask_securest/authorization_providers/role_loaders/abstract_role_loader.py)
that returns a predefined list of roles, for any authenticated subject.

## Usage

The definition of a Role Loader should be included within the definition of an *authorization provider* that supports
it. Example:

```
authorization_provider:
  implementation: flask_securest.authorization_providers.role_based_authorization_provider:RoleBasedAuthorizationProvider
  properties:
    roles_config_file_path: '/opt/manager/roles_config.yaml'
    role_loader:
      name: predefined
      implementation: cloudify_predef_loader.predefined_role_loader:PredefinedRoleLoader
      properties:
        roles:
          - administrator
```

To have this plugin available (in the aforementioned example, through the name "`predefined`"), you will have to
provide a list of REST security plugins as follows:

(In `manager-types.yaml`)

```
  manager.nodes.RestService:
    properties:
      plugins:
        predefined:
          source: <see below>
          [install_args: <see_below>]
```

You can populate `source` and `install_args` in a few ways, as described in [Cloudify's official documentation](http://docs.getcloudify.org/3.4.0/manager/security/):

* `source` referring to a ZIP file URL, representing a packaged Python module. In this case, `install_args` is unneeded.
* `source` referring to a subdirectory relative to the manager blueprint's root. In this case as well, `install_args` is unneeded.
* `source` referring to a Wagon file contained a prepackaged plugin. **This is the recommended approach**. In that case,
  `install_args` should be as follows:
  
  `install_args: 'cloudify-predefined-role-loader --use-wheel --no-index --find-links=wheels/'`
