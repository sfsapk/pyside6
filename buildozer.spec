[app]
title = MyApp
package.name = myapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3, cython==0.29.36, PySide6==6.6.0
orientation = portrait
fullscreen = 0

# Актуальные настройки Android (вместо устаревших)
android.archs = arm64-v8a
android.ndk_path = $HOME/.buildozer/android/platform/android-ndk-r25c
android.sdk_path = $HOME/.buildozer/android/platform/android-sdk
android.min_sdk_version = 21
android.target_sdk_version = 33
android.enable_androidx = True
