# Qubes File Trust

Adds ability to set trust level for files and folders. Untrusted files will be automatically opened in a disposableVM. 

GSoC 2017 project for https://qubes-os.org

Follow the progress [here](https://blog.amorgan.xyz/tag_gsoc-2017.html)!

---

## Notes

With this extension installed, Nautilus will spit out the following error over and over again:

```
** (nautilus:745): CRITICAL **: nautilus_menu_provider_get_background_items: assertion 'NAUTILUS_IS_MENU_PROVIDER (provider)' failed
```

This is a Nautilus bug with extensions, and is tracked here: https://bugzilla.gnome.org/show_bug.cgi?id=784278
