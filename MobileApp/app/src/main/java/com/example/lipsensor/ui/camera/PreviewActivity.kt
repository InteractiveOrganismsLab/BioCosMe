package com.example.lipsensor.ui.camera

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.view.View
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import com.bumptech.glide.Glide
import com.example.lipsensor.R
import com.example.lipsensor.databinding.ActivityPreviewBinding
import com.example.lipsensor.network.MarsApi
import kotlinx.coroutines.launch
import okhttp3.MultipartBody
import okhttp3.RequestBody.Companion.asRequestBody
import java.io.File
import java.lang.Exception
import com.example.lipsensor.MainActivity


class PreviewActivity : AppCompatActivity() {
    private lateinit var binding: ActivityPreviewBinding
    private var savedImageUri: Uri? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Initialize binding
        binding = ActivityPreviewBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Get the Intent that started this activity and extract the string
        savedImageUri = Uri.parse(intent.getStringExtra("EXTRA_SAVED_IMAGE_URI"))
        savedImageUri?.let { uri ->
            Glide.with(this)
                .load(uri)
                .into(binding.imageView)
        }

        // Set click listener for the send button
        binding.buttonS.setOnClickListener {
            Toast.makeText(this, "Sent", Toast.LENGTH_SHORT).show()
            binding.buttonS.visibility = View.INVISIBLE // Make the button invisible
            sendPhoto()
        }

        binding.buttonH.setOnClickListener {
            navigateToHome()
        }
    }

    private fun navigateToHome() {
        val intent = Intent(this, MainActivity::class.java)
        startActivity(intent)
    }

    private fun sendPhoto() {
        savedImageUri?.let { uri ->
            val filePath = uri.path
            if (filePath != null) {
                val file = File(filePath)
                if (file.exists()) {
                    sendImageFile(file)
                } else {
                    Toast.makeText(this, "File not found", Toast.LENGTH_SHORT).show()
                }
            } else {
                // Handle the case where the URI doesn't have a valid file path
                Toast.makeText(this, "Failed to get file path from URI", Toast.LENGTH_SHORT).show()
            }
        } ?: run {
            // Handle the case where savedImageUri is null
            Toast.makeText(this, "No image taken yet.", Toast.LENGTH_SHORT).show()
        }
    }

    private fun sendImageFile(file: File) {
        // Create a multi-part form data part with the request body
        val filePart = MultipartBody.Part.createFormData("files", file.name, file.asRequestBody())

        // Use lifecycleScope.launch to launch a coroutine for the network request
        lifecycleScope.launch {
            try {
                // Make the network request to send the photo
                val response = MarsApi.retrofitService.sendPhotos(filePart)
                if (response.isSuccessful) {
                    val responseBody = response.body()
                    println("Photo sent successfully")
                    // Show the response body if it's not null
                    responseBody?.let { body ->
                        println("Your pH: ${body.predictions}")
                        showPredictions(body.predictions)
                    }
                } else {
                    println("Failed to send photo: ${response.code()}")
                }
            } catch (e: Exception) {
                println("Error sending photo: ${e.message}")
            }
        }
    }

    private fun showPredictions(predictions: List<Double>) {
        val formattedPredictions = predictions.joinToString(separator = ", ") // Convert list to string
        binding.predictionsTextView.text = "Your pH: $formattedPredictions"
        binding.predictionsTextView.visibility = View.VISIBLE // Make TextView visible
    }
}
